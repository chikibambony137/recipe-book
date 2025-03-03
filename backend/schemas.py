from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    description: str
    difficulty: int