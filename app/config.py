# app/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
KEYCLOAK_JWKS_URL = os.getenv("KEYCLOAK_JWKS_URL")
