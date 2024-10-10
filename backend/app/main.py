from fastapi import FastAPI
from .api.router import api_router

# Create a new FastAPI instance with a custom title
app = FastAPI(title="Allergy Management App")

# Include the API router to handle all the routes defined in the api_router
app.include_router(api_router)
