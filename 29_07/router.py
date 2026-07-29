from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import BookCreate
from database import get_db
from services import get_all_book,get_book_detail,add_new_book,update_by_id,delete_by_id,search_book_title,book_by_genre
router = APIRouter(
    prefix="/book",
    tags=["/book"]
)

@router.get("")
def get_book(db:Session = Depends(get_db)):
    return{
        "data": get_all_book(db)
    }

@router.get("/{book_id}")
def get_book_by_id(book_id:int, db:Session = Depends(get_db)):
    return get_book_detail(book_id,db)

@router.post("")
def add_book(book:BookCreate,db:Session=Depends(get_db)):
    return add_new_book(book,db)

@router.put("/{book_id}")
def update_book(book_id,book:BookCreate,db:Session=Depends(get_db)):
    return update_by_id(book_id,book,db)

@router.delete("/{book_id}")
def delete_book(book_id:int,db:Session=Depends(get_db)):
    return delete_by_id(book_id,db)

@router.get("search")
def search_book(book_title:str,db:Session = Depends(get_db)):
    return search_book_title(book_title,db)

@router.get("filter")
def filter_book_genre(book_genre:str,db:Session=Depends(get_db)):
    return book_by_genre(book_genre,db)