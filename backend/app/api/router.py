from fastapi import APIRouter
from .endpoints.allergens import router as allergens_router
from .endpoints.auth import router as auth_router  # Import auth router

api_router = APIRouter()
api_router.include_router(allergens_router, prefix="/allergens", tags=["allergens"])
api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"]) 
