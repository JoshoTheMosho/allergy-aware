from pydantic import BaseModel

class Restaurant(BaseModel):
    restaurant_id: int
    restaurant_name: str