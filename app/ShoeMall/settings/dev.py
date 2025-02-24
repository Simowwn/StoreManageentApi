from .base import *

# Allow requests from frontend
CORS_ALLOW_ALL_ORIGINS = True  # Only use this for development!
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CORS_ALLOW_HEADERS = [
    "authorization",
    "content-type",
    "x-csrftoken",
    "accept",
    "origin",
    "user-agent",
    "x-requested-with",
]

CORS_EXPOSE_HEADERS = ["Content-Type", "X-CSRFToken"]

CORS_URLS_REGEX = r"^/api/.*$"  # Apply CORS only to API routes
