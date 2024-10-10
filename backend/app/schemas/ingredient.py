from pydantic import BaseModel

class Ingredient(BaseModel):
    name: str
    restaurant_id: int
    allergen: str