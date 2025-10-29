from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from comparacion_resultados import obtener_resultados_comparacion 
from healthcare_results import obtener_resultados_healthcare # <--- ¡Importado!

def mostrar_frontend(request):
    """Renderiza el HTML que cargará los datos de la API."""
    return render(request, 'resultados/comparacion.html')

@require_http_methods(["GET"])
def api_comparacion_resultados(request):
    """API endpoint para devolver los resultados de la TAREA 4."""
    resultados = obtener_resultados_comparacion()
    return JsonResponse(resultados, safe=False)

@require_http_methods(["GET"])
def api_healthcare_results(request): # <--- ¡Nueva API!
    """API endpoint para devolver los resultados de Healthcare (U-Net)."""
    resultados = obtener_resultados_healthcare()
    return JsonResponse(resultados, safe=False)
