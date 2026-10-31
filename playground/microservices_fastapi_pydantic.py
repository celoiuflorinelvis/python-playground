import csv
import logging
from datetime import date
from decimal import Decimal
from pathlib import Path
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationInfo
from pandas import DataFrame
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

