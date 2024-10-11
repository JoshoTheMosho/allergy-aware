from fastapi import FastAPI
from .api.router import api_router
from fastapi.middleware.cors import CORSMiddleware

# Create a new FastAPI instance with a custom title
app = FastAPI(title="Allergy Management App")

# Add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow your frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
# Include the API router to handle all the routes defined in the api_router
app.include_router(api_router)
