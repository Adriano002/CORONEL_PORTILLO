from .models import HistorialAlumno, Estudiante, ReporteAlumno
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *


class ReporteListView(ListView):
    model = ReporteAlumno
    template_name = 'reportes/lista.html'


class ReporteCreateView(CreateView):
    model = ReporteAlumno
    form_class = ReporteAlumnoForm
    template_name = 'reportes/formulario.html'
    success_url = reverse_lazy('reporte-lista')


class ReporteUpdateView(UpdateView):
    model = ReporteAlumno
    form_class = ReporteAlumnoForm
    template_name = 'reportes/formulario.html'
    success_url = reverse_lazy('reporte-lista')


class ReporteDeleteView(DeleteView):
    model = ReporteAlumno
    template_name = 'reportes/confirmar_eliminar.html'
    success_url = reverse_lazy('reporte-lista')


def historial_alumno(request, pk):
    estudiante = get_object_or_404(Estudiante, id=pk)
    historial = HistorialAlumno.objects.filter(estudiante=estudiante).first()

    return render(request, 'historial_alumno.html', {
        'estudiante': estudiante,
        'historial': historial,
    })


def detalle_reporte(request, pk):
    reporte = get_object_or_404(ReporteAlumno, pk=pk)

    return render(request, 'reportes/detalle_reporte.html', {
        'reporte': reporte
    })
