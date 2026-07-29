from fastapi import HTTPException
from models import Book
from schema import BookCreate

# lấy tất cả sách
def get_all_book(db):
    return db.query(Book).all()

# lấy sách theo id
def get_book_detail(book_id:int, db):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(
            status_code=404,
            detail= "Khong tim thay sach"
        )
    return{
        "message": "tim thay sach",
        "data" : book
    }

# thêm sách
def add_new_book(book: BookCreate,db):
    new_book = Book(
        title = book.title,
        author = book.author,
        genre = book.genre,
        price = book.price
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return{
        "message" : "them sach thanh cong",
        "data" : new_book
    }

# sửa sách theo id
def update_by_id(book_id: int,update_book:BookCreate,db):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(
            status_code=404,
            detail="khong tim thay sach can sua"
        )
    book.title = update_book.title
    book.author = update_book.author
    book.genre = update_book.genre
    book.price = update_book.price
    db.commit()
    db.refresh(book)
    return{
        "message": "thay doi thanh cong",
        "data": book
    }

# xóa sách theo id
def delete_by_id(book_id:int,db):
    book = db.query(Book).filter(Book.id==book_id).first()
    if book is None:
        raise HTTPException(
            status_code=404,
            detail="khong tim thay sach"
        )
    db.delete(book)
    db.commit()
    return{
        "message":"xoa sach thanh cong",
        "data":book
    }

# tìm kiếm theo tên sách
def search_book_title(book_title:str,db):
    book = db.query(Book).filter(Book.title == book_title).all()
    if book is None:
        raise HTTPException(
            status_code=404,
            detail="khong tim thay sach"
        )
    return{
        "message": "tim thay sach",
        "data": book
    }

# Lọc theo thể loại
def book_by_genre(book_genre:str, db):
    book = db.query(Book).filter(Book.genre == book_genre).all()
    if book is None:
        raise HTTPException(
            status_code=404,
            detail="khong tim thay sach"
        )
    return{
            "message": "tim thay sach",
            "data": book
    }