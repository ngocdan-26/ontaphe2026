from models import Students

def search_student(db,keyword=None,min_age=None,max_age=None,is_active=None,page=1,page_size=10):
    query = db.query(Students)
    if keyword:
        query = query.filter(Students.full_name.ilike(f"%{keyword}%"))

    if min_age is not None:
        query = query.filter(Students.age >= min_age)

    if max_age is not None:
        query = query.filter(Students.age <= max_age)

    if is_active is not None:
        query = query.filter(Students.is_active == is_active)

    total = query.count()
    items = (query.offset((page - 1) * page_size).limit(page_size).all())

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "items": items
    }