"""Base setting admin panel application."""

from pathlib import Path

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

include(
    'components/database.py',
    'components/installed_apps.py',
    'components/middleware.py',
    'components/templates.py',
    'components/auth_password_validators.py',
    'components/constants.py',
    'components/cache.py',
)

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # noqa: WPS407

INTERNAL_IPS = ['127.0.0.1']

LOCALE_PATHS = ['api/locale']  # path to translate
