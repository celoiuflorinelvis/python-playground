"""A small FastAPI users microservice (Python 3.10+).

Install dependencies:
    python -m pip install fastapi uvicorn

Run from this directory:
    python -m uvicorn microservices_fastapi:app --reload --port 5002

Interactive API docs: http://127.0.0.1:5002/docs

Example request:
    curl -X POST http://127.0.0.1:5002/users \
        -H 'Content-Type: application/json' -d '{"name": "Alex", "age": 28}'

Data is held in memory and resets on restart. Use a single worker.
This learning example has no database or authentication.
"""

from itertools import count

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field


class UserInput(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=150)


class User(UserInput):
    id: int


app = FastAPI(title="Users Microservice", version="1.0.0")

users: dict[int, User] = {
    1: User(id=1, name="Mary", age=34),
    2: User(id=2, name="John", age=14),
}
user_ids = count(max(users, default=0) + 1)


@app.get("/health", tags=["Health"])
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/users", response_model=list[User], tags=["Users"])
async def list_users() -> list[User]:
    return list(users.values())


def find_user(user_id: int) -> User:
    user = users.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/users/{user_id}", response_model=User, tags=["Users"])
async def get_user(user_id: int) -> User:
    return find_user(user_id)


@app.post(
    "/users",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
)
async def create_user(payload: UserInput) -> User:
    user = User(id=next(user_ids), name=payload.name, age=payload.age)
    users[user.id] = user
    return user


@app.put("/users/{user_id}", response_model=User, tags=["Users"])
async def update_user(user_id: int, payload: UserInput) -> User:
    find_user(user_id)
    user = User(id=user_id, name=payload.name, age=payload.age)
    users[user_id] = user
    return user


@app.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Users"],
)
async def delete_user(user_id: int) -> Response:
    find_user(user_id)
    del users[user_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)