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
        # Query the Supabase table "dishes" for matching ingredients or allergens
        result = await supabase.table("dishes")\
            .select("*")\
            .or_(f"ingredients.ilike.%{query}%,allergens.ilike.%{query}%")\
            .eq("restaurant_id", user.id)\
            .execute()
        
        # Check for errors in the result
        if result.error:
            raise HTTPException(status_code=500, detail=f"An error occurred: {result.error}")
        
        # Return an empty list if no data is found
        if not result.data:
            return []

        # Return the list of dishes
        return [Dish(**dish) for dish in result.data]
    except Exception as e:
        # Raise an HTTP 500 error if an exception occurs
        raise HTTPException(status_code=500, detail=str(e))