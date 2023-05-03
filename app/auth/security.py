# app/security.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from jose.constants import ALGORITHMS
from app import config
import logging
import requests

logger = logging.getLogger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
KEYCLOAK_JWKS_URL = config.KEYCLOAK_JWKS_URL

def validate_jwt(token: str):
    try:
        payload = jwt.decode(
            token,
            get_keycloak_public_key(),
            algorithms=[ALGORITHMS.RS256],
            options={"verify_signature": True, "verify_aud": False}
        )
        return payload
    except JWTError as e:
        logger.error(f"JWT validation failed: {str(e)}")
        raise HTTPException(status_code=401, detail=str(e))

def get_current_user(token: str = Depends(oauth2_scheme)):
    jwt_payload = validate_jwt(token)
    return jwt_payload

def get_keycloak_public_key():
    jwks = requests.get(KEYCLOAK_JWKS_URL).json()
    return jwks['keys'][0]
