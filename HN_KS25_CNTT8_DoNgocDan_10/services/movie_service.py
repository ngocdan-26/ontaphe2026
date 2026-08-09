from fastapi import HTTPException

from models.movie import Movie


def delete_movie(movie_id, db):

    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Phim không tồn tại"
        )

    if len(movie.tickets) > 0:
        raise HTTPException(
            status_code=400,
            detail="Không thể xóa phim vì đang có vé thuộc phim này"
        )

    db.delete(movie)
    db.commit()

    return {
        "message": "Xóa phim thành công"
    }