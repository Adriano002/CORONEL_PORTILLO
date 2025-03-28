from django import forms
from .models import (
    Estudiante, Padre, Madre, Apoderado,
    AccionRespuesta, Observacion, HistorialAlumno, ReporteAlumno, Tutor
)


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'


class PadreForm(forms.ModelForm):
    class Meta:
        model = Padre
        fields = '__all__'


class MadreForm(forms.ModelForm):
    class Meta:
        model = Madre
        fields = '__all__'


class ApoderadoForm(forms.ModelForm):
    class Meta:
        model = Apoderado
        fields = '__all__'


class AccionRespuestaForm(forms.ModelForm):
    class Meta:
        model = AccionRespuesta
        fields = '__all__'


class ObservacionForm(forms.ModelForm):
    class Meta:
        model = Observacion
        fields = '__all__'


class HistorialAlumnoForm(forms.ModelForm):
    class Meta:
        model = HistorialAlumno
        fields = '__all__'


class ReporteAlumnoForm(forms.ModelForm):
    class Meta:
        model = ReporteAlumno
        fields = '__all__'


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'
