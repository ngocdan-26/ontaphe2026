from pydantic import BaseModel, EmailStr

class StudentResponse(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
