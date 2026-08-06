from pydantic import BaseModel, EmailStr, ConfigDict

class StudentResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    age: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)