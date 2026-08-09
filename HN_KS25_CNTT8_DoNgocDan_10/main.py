from fastapi import FastAPI

from database import Base
from database import engine

from routers.ticket import router as ticket_router
from routers.movie import router as movie_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ticket_router)
app.include_router(movie_router)