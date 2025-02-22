from .base import *

INSTALLED_APPS += [
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be at the top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True  # Temporarily set to True for testing
CORS_ALLOW_CREDENTIALS = False  # Set to False for token authentication

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Add CORS_EXPOSE_HEADERS
CORS_EXPOSE_HEADERS = [
    'authorization',
]

# Remove duplicate settings
# CORS_URLS_REGEX = r"^/api/.*$"  # Remove this if you want all URLs to be accessible

def main():
    """Run administrative tasks."""
    environment = os.environ.get("ENVIRONMENT", "DEV")

    if environment == "PROD":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sample_project.settings.prod")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sample_project.settings.dev")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
