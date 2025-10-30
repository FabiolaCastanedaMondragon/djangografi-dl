"""
Django settings for configuracion project.
...
"""

from pathlib import Path
import os
import environ # <--- Importación de environ

# Inicializa environ y lee el archivo .env si existe (para pruebas locales)
env = environ.Env(
    # Establece DEBUG por defecto a False si no se encuentra
    DEBUG=(bool, False)
)
# Lee el archivo .env si existe (útil para pruebas locales)
environ.Env.read_env(os.path.join(Path(__file__).resolve().parent.parent, '.env'))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# AHORA LEE LA CLAVE SEGURA DESDE LA VARIABLE DE ENTORNO 'SECRET_KEY'
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# LEE LA VARIABLE DE ENTORNO 'DEBUG', por defecto es False en producción
DEBUG = env('DEBUG')

# PERMITE ACCESO DESDE CUALQUIER HOST (Necesario para Render.com)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['.render.com'])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'resultados',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # NUEVO: Middleware de WhiteNoise para servir archivos estáticos en producción
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'configuracion.urls'

# --- INICIO DEL BLOQUE TEMPLATES FALTANTE (SOLUCIÓN admin.E403) ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True, # CRUCIAL para el admin y plantillas de apps
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
# --- FIN DEL BLOQUE TEMPLATES FALTANTE ---


WSGI_APPLICATION = 'configuracion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    # CONFIGURACIÓN PARA POSTGRESQL EN RENDER
    'default': env.db_url(
        'DATABASE_URL', # Render proporciona esta URL
        # Si no la encuentra, usa SQLite (útil para pruebas locales)
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'
    )
}


# ... (Password validation e Internationalization permanecen igual) ...


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# NUEVO: Directorio donde Django recolectará los archivos estáticos en Render
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuración adicional para evitar problemas de CORS/CSRF en producción
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=['https://*.render.com'])


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'