from django.urls import path
from . import views

urlpatterns = [
    # Ruta principal: Muestra el Frontend (el HTML)
    path('', views.mostrar_frontend, name='frontend_comparacion'), 
    
    # API 1: Tarea 4 (Comparación de Arquitecturas)
    path('api/v1/comparacion/', views.api_comparacion_resultados, name='api_comparacion_resultados'),
    
    # API 2: Resultados Healthcare (U-Net)
    path('api/v1/healthcare/', views.api_healthcare_results, name='api_healthcare_results'),
]
