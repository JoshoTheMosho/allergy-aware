from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List
from ...core.config import supabase
from ..dependencies.get_user import get_current_user
from ...schemas.dish import Dish
from ...schemas.ingredient import Ingredient
from ...schemas.restaurant import Restaurant

router = APIRouter()

@router.get("/search/", response_model=List[Dish])
async def search_ingredients(query: str = Query(..., title="Query", description="Search by allergen or ingredient"), user=Depends(get_current_user)):
    try:
        result = await supabase.table("dishes")\
            .select("*")\
            .or_(f"ingredients.ilike.%{query}%,allergens.ilike.%{query}%")\
            .eq("restaurant_id", user.id)\
            .execute()
        
        if result.error:
            raise HTTPException(status_code=500, detail=f"An error occurred: {result.error}")
        if not result.data:
            return []

        return [Dish(**dish) for dish in result.data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))