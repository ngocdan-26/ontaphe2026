from pydantic import BaseModel, EmailStr, Field

class StudentCreate(BaseModel):
    full_name: str = Field(min_length=1)
    email: EmailStr
    age: int = Field(ge=18, le=60)