
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from services.movie_service import delete_movie

router = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)


@router.delete("/{movie_id}")
def remove_movie(
    movie_id: int,
    db: Session = Depends(get_db)
):
    delete_movie(movie_id, db)

    return {
        "statusCode": 200,
        "error": None,
        "message": "Xóa phim thành công",
        "data": None
    }