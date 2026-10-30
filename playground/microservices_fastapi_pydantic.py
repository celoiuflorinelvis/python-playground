import logging
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from pandas import DataFrame
from typing import Annotated
import operator

print("Microservices FastAPI Pydantic Playground")

