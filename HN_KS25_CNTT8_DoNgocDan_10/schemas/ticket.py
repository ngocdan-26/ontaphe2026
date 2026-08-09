from pydantic import BaseModel,ConfigDict,Field
from schemas.movie import MovieResponse

class TicketCreate(BaseModel):
    ticket_code: str = Field(min_length=6,max_length=20)
    seat_number: str = Field(min_length=2,max_length=10)
    price: float = Field(gt=0)
    movie_id: int

class TicketResponse(BaseModel):
    ticket_code: str
    seat_number: str
    price: float
    movie: MovieResponse
    model_config = ConfigDict(from_attributes=True)