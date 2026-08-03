from pydantic import BaseModel, EmailStr

class StudentResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True