from pydantic import BaseModel

class Dish(BaseModel):
    name: str
    ingredient: str
    restaurant_id: int