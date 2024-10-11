from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List
from ...core.config import supabase
from ..dependencies.get_user import get_current_user
from ...schemas.dish import Dish
from ...schemas.ingredient import Ingredient
from ...schemas.restaurant import Restaurant

# Create a new APIRouter instance
router = APIRouter()

@router.get("/search/", response_model=List[Dish])
def search_ingredients(query: str = Query(..., title="Query", description="Search by allergen or ingredient"), user=Depends(get_current_user)):
    """
    Search for dishes based on allergens or ingredients.

    Args:
        query (str): The search query string. This parameter is used to search for dishes by allergen or ingredient.
        user: The current authenticated user. This parameter is automatically injected by FastAPI using the get_current_user dependency.

    Returns:
        List[Dish]: A list of dishes that match the search query.

    Raises:
        HTTPException: If an error occurs while processing the request.
    """
    try:

        # Step 1: Query the "user" table to get the associated restaurant_id for the current user
        user_result = supabase.table("users")\
            .select("restaurant_id")\
            .eq("id", user.user.id)\
            .maybe_single()\
            .execute()

        print("User Result:", user_result.data)

        restaurant_id = user_result.data["restaurant_id"]

        print("Restaurant ID:", restaurant_id)

        # Step 2: Query the Ingredients table based on the ingredient name or allergen
        ingredient_result = supabase.table("ingredients")\
            .select("*")\
            .or_(f"name.ilike.%{query}%,allergen.ilike.%{query}%")\
            .eq("restaurant_id", restaurant_id)\
            .execute()

         # Extract the list of ingredients found
        ingredients_data = ingredient_result.data
        if not ingredients_data:
            return []

        print("Ingredients Data:", ingredients_data)

        # Step 3: Get a list of ingredient names to find matching dishes
        ingredient_names = [ingredient['name'] for ingredient in ingredients_data]

        # Step 4: Query the Dishes table to find dishes containing these ingredients
        dish_result = supabase.table("dishes")\
            .select("*")\
            .in_("ingredient", ingredient_names)\
            .eq("restaurant_id", restaurant_id)\
            .execute()
        
        print("Ingredient Names:", ingredient_names)

        # Return the list of dishes if found, otherwise an empty list
        return [Dish(**dish) for dish in dish_result.data] if dish_result.data else []
    
    except HTTPException as http_exc:
        # If an HTTPException is raised, re-raise it
        raise http_exc
    
    except Exception as e:
        # Raise an HTTP 500 error if an exception occurs
        raise HTTPException(status_code=500, detail=str(e))