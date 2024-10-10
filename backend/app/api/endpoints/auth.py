from fastapi import APIRouter, HTTPException, Body
from supabase import AuthApiError
from ...core.config import supabase

router = APIRouter()

@router.post("/login/")
async def login_user(email: str = Body(...), password: str = Body(...)):
    """
    Authenticate a user and return access and refresh tokens along with user details.

    Args:
        email (str): The email address of the user.
        password (str): The password of the user.

    Returns:
        dict: A dictionary containing the access token, refresh token, token type, expiration time, and user details.

    Raises:
        HTTPException: If authentication fails.
    """
    try:
        # Authenticate the user with Supabase
        response = await supabase.auth.sign_in_with_password({"email": email, "password": password})

        # Extract token details from the session
        session_info = response.get('session', {})
        access_token = session_info.get('access_token')
        refresh_token = session_info.get('refresh_token')
        token_type = session_info.get('token_type')  # Typically "bearer"
        expires_in = session_info.get('expires_in')
        
        # Include user details
        user_info = response.get('user', {})

        return {
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": token_type,
            "expires_in": expires_in,
            "user": user_info
        }
    
    except AuthApiError as e:
        # If authentication fails, raise an HTTP 401 Unauthorized exception
        raise HTTPException(status_code=401, detail="Invalid email or password.") 
    except Exception as e:
        # For other unexpected errors, raise a 500 Internal Server Error
        raise HTTPException(status_code=500, detail="An internal server error occurred.")
    

