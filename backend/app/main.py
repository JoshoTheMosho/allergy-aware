from fastapi import FastAPI
from .api.router import api_router

app = FastAPI(title="Allergy Management App")

app.include_router(api_router)
