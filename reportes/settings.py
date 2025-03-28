from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-_kvac$em4&j73!@&*rp^a^1oivgn8ul8p#&$5(tv!qcx6t)^gs'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.51']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'alumnos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'reportes.urls'

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

WSGI_APPLICATION = 'reportes.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}



JAZZMIN_SETTINGS = {
    "site_title": "Sistema de Reportes",
    "site_header": "Panel de Administración",
    "site_brand": "Sistema TOECE",
    "welcome_sign": "Bienvenido al Panel de Reportes",
    "copyright": "Sistema TOECE © 2025",
    "search_model": ["alumnos.ReporteAlumno"],
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "alumnos.ReporteAlumno": "fas fa-file-alt",
    },
    "custom_css": "admin/css/custom_admin.css",
    "custom_js": "admin/js/custom_admin.js",
    "widgets": {
        "auth.User": "total",
        "alumnos.ReporteAlumno": "chart",
    },
    "theme": "solar",
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
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
