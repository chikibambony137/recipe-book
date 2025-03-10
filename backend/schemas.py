from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    description: str
    difficulty: int

class User(BaseModel):
    login: str
    password: str