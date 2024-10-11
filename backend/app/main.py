import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.router import api_router

# Create a new FastAPI instance with a custom title
app = FastAPI(title="Allergy Management App")

# Set up the environment variable for development
is_development = os.getenv("ENVIRONMENT") == "development"

if is_development:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # Allow your frontend URL only in development
        allow_credentials=True,
        allow_methods=["*"],  # Allow all HTTP methods
        allow_headers=["*"],  # Allow all headers
    )


# Include the API router to handle all the routes defined in the api_router
app.include_router(api_router)
