from datetime import timedelta
from pathlib import Path
import environ
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
import dj_database_url


env = environ.Env()
environ.Env.read_env()
ENVIRONMENT = env

cloudinary.config(
    cloud_name=os.environ.get('CLOUD_NAME'),
    api_key=os.environ.get('CLOUD_API_KEY'),
    api_secret=os.environ.get('CLOUD_API_SECRET'),
    secure=True
)

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY')
DOMAIN = os.environ.get('DOMAIN')
DEBUG = os.environ.get('DEBUG')
FRONTEND_URL = os.environ.get('FRONTEND_URL')

ALLOWED_HOSTS = [
    "*"
]


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # THIRD PARTY APPS
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django.contrib.sites',
    'cloudinary',
    'drf_yasg',

    # AUTH APPS
    'dj_rest_auth',
    'dj_rest_auth.registration',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # LOCAL APPS
    'apps.user',
    # 'apps.identify',

]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_EMAIL_REQUIRED = False

REST_USE_JWT = True


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'USER_ID_FIELD': 'userId',
    'USER_ID_CLAIM': 'user_id',
    'SIGNING_KEY': os.environ.get('JWT_SECRET_KEY'),
}


CSRF_TRUSTED_ORIGINS = [
    'https://server.tonis.site',
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',

    # flutter port
    'http://localhost:8080',
    'http://127.0.0.1:8080',


    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',

    'https://server.tonis.site',
]
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',

    # flutter port
    'http://localhost:8080',
    'http://127.0.0.1:8080',

    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',

    'https://server.tonis.site',
]


CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'user.CustomUserModel'


ACCOUNT_AUTHENTICATION_METHOD = 'username'
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'apps.user.serializers.CustomUserModelSerializer',
    # 'LOGIN_SERIALIZER': 'dj_rest_auth.serializers.LoginSerializer',
    'TOKEN_SERIALIZER': 'dj_rest_auth.serializers.TokenSerializer',
    'JWT_SERIALIZER': 'dj_rest_auth.serializers.JWTSerializer',
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        'rest_framework.permissions.AllowAny',
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
}


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# SITE_ID = 1
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
SITE_ID = 2

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Lima'


USE_I18N = True

USE_TZ = False

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

SITE_NAME = ('BESAFE')
JAZZMIN_SETTINGS = {
    "site_title": "BESAFE",
    "site_header": "BESAFE",
    "site_brand": "BESAFE",

    "welcome_sign": "Bienvenido a BESAFE Admin",
    "copyright": "BESAFE",

    "topmenu_links": [
        {"name": "Home",  "url": "admin:index",
            "permissions": ["auth.view_user"]},
        {"model": "user.CustomUserModel"},
        {"app": "enterprise"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    # "hide_apps": [
    #     "auth",
    #     "social_django",
    #     "rest_framework_simplejwt",
    #     "token_blacklist"
    # ],
    # "hide_models": [
    #     "cart.CartItem",
    #     "order.OrderItem",
    #     "account.UserAddress",
    #     "product.CharacteristicProduct",
    #     "product.ProductImage",
    # ],
    # "order_with_respect_to": ["user", "product", "order", "shipping", "coupon", "cart", "account"],

    # "icons": {
    #     "user.UserAccount": "fas fa-user",
    #     "product.brand": "fas fa-copyright",
    #     "product.category": "fas fa-boxes",
    #     "product.CharacteristicProduct": "fas fa-list",
    #     "product.ProductImage": "fas fa-image",
    #     "product.Product": "fas fa-dolly",
    #     "order.Order": "fas fa-box-open",
    #     "shipping.Shipping": "fas fa-truck",
    #     "coupon.Coupon": "fas fa-tags",
    #     "cart.Cart": "fas fa-shopping-cart",
    #     "account.UserProfile": "fas fa-user-circle",
    # },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fa fa-check",

}
JAZZMIN_UI_TWEAKS = {
    "brand_colour": "navbar-success",
    "accent": "accent-navy",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": True,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_child_indent": True,
    "theme": "minty",
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "site_brand": "BESAFE",
}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
