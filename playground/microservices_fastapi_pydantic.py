import csv
import logging
from pathlib import Path
from datetime import date, datetime
from decimal import Decimal
from fastapi import FastAPI, HTTPException, Depends, Request, Security, status, APIRouter, Path as FastAPIPath, Query
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationInfo
from pandas import DataFrame, concat
from typing import Annotated, Optional, Type, TypeVar
import operator

print("Microservices FastAPI Pydantic Playground")

# logging.basicConfig({
#     "level": logging.INFO,
#     "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# })
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)
logger = logging.getLogger("orders-api")

logger.info("Starting the FastAPI microservices playground")
logger.error("This is an error message")
logger.warning("This is a warning message")
logger.debug("This is a debug message")

IdentifierInt = Annotated[int, "Identifiers, should be positive",  Field(gt=0)]
DateReq = Annotated[date, Field(description="Required date")]
StringReq = Annotated[str, Field(description="Required string", min_length=1)]

T = TypeVar("T", bound=BaseModel)

class User(BaseModel):
    id: IdentifierInt
    name: str
    email: EmailStr
    address: str
    city: str
    country: str
    phone: str  # must come after country so info.data["country"] is available in validator
    created_at: DateReq = Field(default_factory=date.today)

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str, info: ValidationInfo) -> str:
        country_code = info.data.get("country")
        if not country_code:
            return v
        match = df_phone_prefixes[df_phone_prefixes["country_code"] == country_code]
        if match.empty:
            raise ValueError(f"No phone prefix found for country code: {country_code}")
        prefix = match.iloc[0]["phone_prefix"]
        if not v.startswith(prefix):
            raise ValueError(f"Phone must start with {prefix} for country {country_code}")
        return v


class Product(BaseModel):
    id: IdentifierInt
    name: str
    category: str
    brand: str
    sku: str
    description: str
    stock_quantity: int

    @field_validator("stock_quantity")
    @classmethod
    def must_be_non_negative(cls, v: int) -> int:
        if v < 0:
            raise ValueError("stock_quantity must be >= 0")
        return v


class Order(BaseModel):
    id: IdentifierInt
    user_id: IdentifierInt
    order_date: DateReq
    status: str
    shipping_address: str
    city: str
    country: str
    total_amount: Decimal


class OrderItem(BaseModel):
    id: IdentifierInt
    order_id: IdentifierInt
    product_id: IdentifierInt
    quantity: int
    unit_price: Decimal
    subtotal: Decimal

    @field_validator("quantity")
    @classmethod
    def must_be_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("quantity must be > 0")
        return v


class Price(BaseModel):
    id: IdentifierInt
    product_id: IdentifierInt
    price: Decimal
    currency: str
    valid_from: DateReq
    valid_to: Optional[DateReq] = None  # None means the price is currently active


class PhonePrefixes(BaseModel):
    country_code: StringReq
    country_name: StringReq
    phone_prefix: StringReq

def load_from_csv(path: Path | str, target: Type[T]) -> list[T]:
    with Path(path).open(newline="", encoding="utf-8") as f:
        return [target(**{k: v if v != "" else None for k, v in row.items()}) for row in csv.DictReader(f)]

def load_phone_prefixes() -> list[PhonePrefixes]:
    csv_path = Path(__file__).parent / "data" / "country_phone_prefixes.csv"
    return load_from_csv(csv_path, PhonePrefixes)

# Load phone prefixes from the CSV file at startup
_CSV_MODEL_MAP: dict[str, Type[BaseModel]] = {
    "users": User,
    "products": Product,
    "orders": Order,
    "order_items": OrderItem,
    "prices": Price,
    "country_phone_prefixes": PhonePrefixes,
}

# Load phone prefixes first — User.validate_phone depends on df_phone_prefixes
_data_dir = Path(__file__).parent / "data"
df_phone_prefixes = DataFrame([r.model_dump() for r in load_from_csv(_data_dir / "country_phone_prefixes.csv", PhonePrefixes)])
datasets: dict[str, DataFrame] = {"country_phone_prefixes": df_phone_prefixes}

for _csv_file in sorted(_data_dir.glob("*.csv")):
    if _csv_file.stem in datasets:
        continue  # already loaded above
    _model_cls = _CSV_MODEL_MAP.get(_csv_file.stem)
    if _model_cls is None:
        logger.warning("No model mapped for %s, skipping", _csv_file.name)
        continue
    _records = load_from_csv(_csv_file, _model_cls)
    datasets[_csv_file.stem] = DataFrame([r.model_dump() for r in _records])
    logger.info("Loaded %d records from %s", len(_records), _csv_file.name)

# --- Authentication ---
_api_key_scheme = APIKeyHeader(name="X-API-Key", auto_error=True)
VALID_API_KEYS = {"your_api_key_here"}

def verify_api_key(api_key: str = Security(_api_key_scheme)) -> None:
    if api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid API key")

# --- Tracing ---
def trace_request(request: Request) -> None:
    logger.info("Tracing request: %s %s", request.method, request.url)

# define the FastAPI application instance
app = FastAPI(
    title="E-Commerce FastAPI Microservices App",
    description="An example FastAPI application for managing e-commerce microservices",
    version="1.0",
    summary="E-Commerce FastAPI Microservices App",
    docs_url="/docs",
    redoc_url="/redoc",
    swagger_ui_parameters={"persistAuthorization": True},
    dependencies=[Security(verify_api_key), Depends(trace_request)],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    logger.warning("HTTP %d on %s: %s", exc.status_code, request.url, exc.detail)
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    logger.warning("Validation error on %s: %s", request.url, exc.errors())
    return JSONResponse(
        status_code=422,
        content={"error": "Validation failed", "details": exc.errors()},
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.error("Unhandled error on %s: %s", request.url, exc, exc_info=True)
    return JSONResponse(status_code=500, content={"error": "Internal server error"})


# --- API Router ---
router = APIRouter(prefix="/api/v1")


@router.get("/users",
    summary="Get all users",
    response_model=list[User],
    response_description="List of all users",
    status_code=status.HTTP_200_OK
)
def get_users() -> list[User]:
    """
    Get all users.

    Returns:
        list[User]: get all users
    """

    df_users = datasets.get("users")
    if df_users is None:
        raise HTTPException(status_code=404, detail="Users datasource was not found")

    return [User(**row) for row in df_users.to_dict(orient="records")]


@router.get("/users/search",
    summary="Search users",
    response_model=list[User],
    response_description="List of users matching the query",
    status_code=status.HTTP_200_OK
)
def search_users(
    query: Annotated[str, Query(title="Query", description="The query string to search for in user names or emails")]
) -> list[User]:
    """
    Search users by a query string.

    Args:
        query (str): The query string to search for in user names or emails.

    Raises:
        HTTPException: If the users datasource was not found.

    Returns:
        list[User]: List of users matching the query.
    """

    df_users = datasets.get("users")
    if df_users is None:
        raise HTTPException(status_code=404, detail="Users datasource was not found")
    
    filtered_users = df_users.query(query)
    if filtered_users.empty:
        raise HTTPException(status_code=404, detail="No users found matching the query")
    
    return [User(**row) for row in filtered_users.to_dict(orient="records")]


@router.get("/users/{user_id}",
    summary="Get user by ID",
    response_model=User | None,
    response_description="The user with the specified ID",
    status_code=status.HTTP_200_OK
)
def get_user_by_id(
    user_id: Annotated[int, FastAPIPath(title="User ID", description="The ID of the user to retrieve")]
) -> User | None:
    """
    Get user by ID.

    Args:
        user_id (Annotated[int, FastAPIPath, optional): The ID of the user to retrieve.

    Raises:
        HTTPException: If the users datasource was not found.
        HTTPException: If the user with the specified ID was not found.

    Returns:
        User | None: The user with the specified ID, or None if not found.
    """

    logging.info("Fetching user with ID %d", user_id)
    df_users = datasets.get("users")
    if df_users is None:
        raise HTTPException(status_code=404, detail="Users datasource was not found")
    user_row = df_users[df_users["id"] == user_id]
    if user_row.empty:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**user_row.iloc[0].to_dict())


@router.delete("/users/{user_id}",
    summary="Delete user by ID",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
    user_id: Annotated[int, FastAPIPath(title="User ID", description="The ID of the user to delete")]
) -> None:
    """
    Delete a user by ID.

    Args:
        user_id (int): The ID of the user to delete.

    Raises:
        HTTPException: If the users datasource was not found.
        HTTPException: If the user with the specified ID was not found.
    """

    df_users = datasets.get("users")
    if df_users is None:
        raise HTTPException(status_code=404, detail="Users datasource was not found")
    user_index = df_users.index[df_users["id"] == user_id].tolist()
    if not user_index:
        raise HTTPException(status_code=404, detail="User not found")
    df_users.drop(user_index[0], inplace=True)


# --- Create a new user or update an existing user ---

# Request model for creating a new user
class CreateUserRequest(BaseModel):
    """
    Request model for creating a new user.

    Args:
        BaseModel (_type_): The base class for Pydantic models.
    """
    
    name: Annotated[str, Field(title="Name", description="The name of the user", min_length=1)]
    email: Annotated[EmailStr, Field(title="Email", description="The email of the user")]
    address: Annotated[str, Field(title="Address", description="The address of the user", min_length=1)]
    city: Annotated[str, Field(title="City", description="The city of the user", min_length=1)]
    country: Annotated[str, Field(title="Country", description="The country of the user", min_length=1)]
    phone: Annotated[str, Field(title="Phone", description="The phone number of the user")]  # must come after country so info.data["country"] is available in validator
    created_at: DateReq = Field(default_factory=date.today)
    
    
    def validate_name_and_email_uq(cls, v: str, info: ValidationInfo) -> str:
        """Validate that the combination of name and email is unique.

        Args:
            v (str): The value of the field being validated.
            info (ValidationInfo): The validation info containing other field values.

        Raises:
            ValueError: If a user with the same name and/or email already exists.

        Returns:
            str: The validated value of the field.
        """
        
        df_users = datasets.get("users")
        if df_users is None:
            return v
        if "name" in info.data and "email" in info.data:
            name = info.data["name"]
            email = info.data["email"]
            if not df_users[(df_users["name"] == name) | (df_users["email"] == email)].empty:
                raise ValueError(f"User with name '{name}' and/or email '{email}' already exists")
        return v
    
    
    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str, info: ValidationInfo) -> str:
        return cls.validate_name_and_email_uq(cls, v, info)

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str, info: ValidationInfo) -> str:
        return cls.validate_name_and_email_uq(cls, v, info)
    
    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str, info: ValidationInfo) -> str:
        country_code = info.data.get("country")
        if not country_code:
            return v
        match = df_phone_prefixes[df_phone_prefixes["country_code"] == country_code]
        if match.empty:
            raise ValueError(f"No phone prefix found for country code: {country_code}")
        prefix = match.iloc[0]["phone_prefix"]
        if not v.startswith(prefix):
            raise ValueError(f"Phone must start with {prefix} for country {country_code}")
        return v
        
# Request model for updating an existing user
class UpdateUserRequest(BaseModel):
    """
    Request model for updating an existing user.

    Args:
        BaseModel (_type_): The base class for Pydantic models.
    """
    
    name: Annotated[Optional[str], Field(title="Name", description="The name of the user", min_length=1)]
    email: Annotated[Optional[EmailStr], Field(title="Email", description="The email of the user")]
    address: Annotated[Optional[str], Field(title="Address", description="The address of the user", min_length=1)]
    city: Annotated[Optional[str], Field(title="City", description="The city of the user", min_length=1)]
    country: Annotated[Optional[str], Field(title="Country", description="The country of the user", min_length=1)]
    phone: Annotated[Optional[str], Field(title="Phone", description="The phone number of the user")]  # must come after country so info.data["country"] is available in validator
    
    
    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str, info: ValidationInfo) -> str:
        country_code = info.data.get("country")
        if not country_code or not info.data.get("phone"):
            return v
        match = df_phone_prefixes[df_phone_prefixes["country_code"] == country_code]
        if match.empty:
            raise ValueError(f"No phone prefix found for country code: {country_code}")
        prefix = match.iloc[0]["phone_prefix"]
        if not v.startswith(prefix):
            raise ValueError(f"Phone must start with {prefix} for country {country_code}")
        return v

@router.post("/users",
    summary="Create a new user",
    response_model=CreateUserRequest,
    response_description="The created user",
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user: CreateUserRequest
) -> CreateUserRequest:
    """
    Create a new user.

    Args:
        user (CreateUserRequest): The user to create.

    Raises:
        HTTPException: If the users datasource was not found.

    Returns:
        CreateUserRequest: The created user.
    """

    df_users = datasets.get("users")
    if df_users is None:
        raise HTTPException(status_code=404, detail="Users datasource was not found")
    
    # Generate new ID
    new_id = len(df_users) + 1
    
    new_user = User(id=new_id, **user.model_dump())
    
    df_users = concat([df_users, DataFrame([new_user.model_dump()])], ignore_index=True)
    datasets["users"] = df_users
    return new_user


@router.put("/users/{user_id}",
    summary="Update an existing user",
    response_model=User,
    response_description="The updated user",
    status_code=status.HTTP_200_OK
)
def update_user(
    user_id: Annotated[int, FastAPIPath(description="The ID of the user to update")],
    user: UpdateUserRequest
) -> User:
    """
    Update an existing user.

    Args:
        user_id (int): The ID of the user to update.
        user (UpdateUserRequest): The updated user data.

    Raises:
        HTTPException: If the users datasource was not found or the user was not found.

    Returns:
        User: The updated user.
    """

    df_users = datasets.get("users")
    if df_users is None:
        raise HTTPException(status_code=404, detail="Users datasource was not found")

    idx_user = df_users["id"] == user_id
    if not idx_user.any():
        raise HTTPException(status_code=404, detail="User not found")

    crt_user = df_users.loc[idx_user].iloc[0].to_dict()

    # Merge: only override fields that were explicitly provided (non-None)
    update_fields = {k: v for k, v in user.model_dump().items() if v is not None}
    crt_user.update(update_fields)

    updated_user = User(**crt_user)

    for col, val in updated_user.model_dump().items():
        df_users.loc[idx_user, col] = val
    datasets["users"] = df_users

    logger.info("Updated user ID %d: %s", user_id, update_fields)
    return updated_user


app.include_router(router)

