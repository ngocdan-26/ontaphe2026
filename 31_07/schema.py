from pydantic import BaseModel, EmailStr, Field

class StudentCreate(BaseModel):
    student_code: str = Field(min_length=1)
    full_name: str = Field(min_length=1)
    email: EmailStr
    age: int = Field(ge=18, le=60)
    is_active: bool