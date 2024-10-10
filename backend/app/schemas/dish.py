from pydantic import BaseModel

class Dish(BaseModel):
    """
    Represents a dish with its name, ingredient, and associated restaurant ID.

    Attributes:
        name (str): The name of the dish.
        ingredient (str): The main ingredient of the dish.
        restaurant_id (int): The ID of the restaurant that offers the dish.
    """
    name: str
    ingredient: str
    restaurant_id: int