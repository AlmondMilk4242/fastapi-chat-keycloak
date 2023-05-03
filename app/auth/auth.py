from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from .security import get_current_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def authenticate_user(token: str = Depends(oauth2_scheme)):
    user_data = get_current_user(token)
    if user_data:
        return user_data
    raise HTTPException(status_code=401, detail="Invalid access token")
