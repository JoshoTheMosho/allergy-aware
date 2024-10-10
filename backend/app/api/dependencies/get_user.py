from fastapi import HTTPException, Depends, Header
from ...core.config import supabase
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = await supabase.auth.api.get_user(token)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user
