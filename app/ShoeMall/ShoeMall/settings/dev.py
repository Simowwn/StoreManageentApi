from .base import *

INSTALLED_APPS += []
MIDDLEWARE += []

CORS_URLS_REGEX = r"^/api/.*$"
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:8000",
    "http://localhost:8001",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:8000",
    "http://localhost:8001",
]

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
