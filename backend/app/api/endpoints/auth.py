# src/api/endpoints/auth.py

from fastapi import APIRouter, HTTPException, Body
from ...core.config import supabase

router = APIRouter()

@router.post("/login/")
async def login_user(email: str = Body(...), password: str = Body(...)):
    user, error = await supabase.auth.sign_in(email=email, password=password)
    if error:
        raise HTTPException(status_code=400, detail=str(error.message))
    return {"message": "Login successful", "session": user}
