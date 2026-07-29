from pydantic import BaseModel, Field
from decimal import Decimal

class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    genre: str = Field(min_length=1, max_length=50)
    price: Decimal = Field(gt=0)