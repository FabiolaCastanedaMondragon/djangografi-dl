from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluir las rutas de la aplicación 'resultados'
    path('', include('resultados.urls')), 
]
