from django.urls import path
from .views import ReporteListView, ReporteCreateView, ReporteUpdateView, ReporteDeleteView, historial_alumno, detalle_reporte

urlpatterns = [
    path('reportes/', ReporteListView.as_view(), name='reporte-lista'),
    path('reportes/nuevo/', ReporteCreateView.as_view(), name='reporte-nuevo'),
    path('reportes/editar/<int:pk>/',
         ReporteUpdateView.as_view(), name='reporte-editar'),
    path('reportes/eliminar/<int:pk>/',
         ReporteDeleteView.as_view(), name='reporte-eliminar'),
    path('historial/<int:pk>/', historial_alumno, name='historial_alumno'),
    path('reporte/<int:pk>/', detalle_reporte, name='detalle-reporte'),
]
