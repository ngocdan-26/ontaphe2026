from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Students(Base):
    __tablename__ = "students"

    student_code = Column(String(20), primary_key=True)
    full_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)