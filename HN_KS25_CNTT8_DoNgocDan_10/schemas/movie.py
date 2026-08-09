from pydantic import BaseModel,ConfigDict,Field

class MovieCreate(BaseModel):
    name: str = Field(min_length=1,max_length=100)
    director: str = Field(min_length=1,max_length=100)

class MovieResponse(BaseModel):
    name: str
    director: str
    model_config = ConfigDict(from_attributes=True)