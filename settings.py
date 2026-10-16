INSTALLED_APPS = [
    # ... aplicaciones por defecto de django
    'corsheaders',  # <--- Añadir esta línea
    'rest_framework',
    'gimnasio',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # <--- Colocar siempre al principio
    'django.middleware.common.CommonMiddleware',
    # ... otros middlewares
]

# Configuración permitida para desarrollo local
CORS_ALLOW_ALL_ORIGINS = True 

# O si deseas restringirlo específicamente a tu entorno frontend:
# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:5500",
#     "http://localhost:5500",
#  ]
