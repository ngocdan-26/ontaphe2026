from fastapi import APIRouter, Depends,Query
from sqlalchemy.orm import Session
from database import get_db
from services import search_student
router = APIRouter(
    prefix="/students",
    tags=["/students"]
)

@router.get("/search")
def search_students(
    keyword: str | None = None,
    min_age: int | None = None,
    max_age: int | None = None,
    is_active: bool | None = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return search_student(
        db=db,
        keyword=keyword,
        min_age=min_age,
        max_age=max_age,
        is_active=is_active,
        page=page,
        page_size=page_size
    )