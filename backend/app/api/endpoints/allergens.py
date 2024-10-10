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
async def search_ingredients(query: str = Query(..., title="Query", description="Search by allergen or ingredient"), user=Depends(get_current_user)):
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
        
        # Step 1: Query the Ingredients table based on the ingredient name or allergen
        ingredient_result = await supabase.table("ingredients")\
            .select("*")\
            .or_(f"name.ilike.%{query}%,allergen.ilike.%{query}%")\
            .eq("restaurant_id", user.user.id)\
            .execute()

         # Extract the list of ingredients found
        ingredients_data = ingredient_result.data
        if not ingredients_data:
            return []
        
         # Step 2: Get a list of ingredient names to find matching dishes
        ingredient_names = [ingredient['name'] for ingredient in ingredients_data]

        # Step 3: Query the Dishes table to find dishes containing these ingredients
        dish_result = await supabase.table("dishes")\
            .select("*")\
            .in_("ingredient", ingredient_names)\
            .eq("restaurant_id", user.user.id)\
            .execute()

         # Return the list of dishes if found, otherwise an empty list
        return [Dish(**dish) for dish in dish_result.data] if dish_result.data else []
    
    except Exception as e:
        # Raise an HTTP 500 error if an exception occurs
        raise HTTPException(status_code=500, detail=str(e))