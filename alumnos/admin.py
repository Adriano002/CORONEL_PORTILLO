from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin
from .models import (
    AccionRespuesta, Apoderado, Tutor, Estudiante, HistorialAlumno,
    Madre, Observacion, Padre, ReporteAlumno
)


@admin.register(AccionRespuesta)
class AccionRespuestaAdmin(admin.ModelAdmin):
    # Cambia fecha a get_fecha si es necesario
    list_display = ('nombre','estudiante')
    search_fields = ('nombre','estudiante')


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'grado', 'seccion', 'nombredeseccion')
    search_fields = ('nombre', 'dni', 'grado', 'seccion')
    list_filter = ('grado', 'seccion')


@admin.register(HistorialAlumno)
class HistorialAlumnoAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'grado', 'seccion',
                    'nombredeseccion', 'cantidad_reportes', 'fecha')
    search_fields = ('estudiante__nombre', 'reportes__condicion')
    list_filter = ('estudiante__grado', 'estudiante__seccion')

    def grado(self, obj):
        return obj.estudiante.grado if obj.estudiante else "Sin grado"

    def seccion(self, obj):
        return obj.estudiante.seccion if obj.estudiante else "Sin sección"

    def nombredeseccion(self, obj):
        return obj.estudiante.nombredeseccion if obj.estudiante else "Sin nombre"

    def cantidad_reportes(self, obj):
        return obj.reportes.count()

    grado.short_description = "Grado"
    seccion.short_description = "Sección"
    nombredeseccion.short_description = "Nombre de la Sección"
    cantidad_reportes.short_description = "Cantidad de Reportes"


@admin.register(Padre)
class PadreAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'celular', 'mostrar_estudiantes')
    search_fields = ('nombre', 'celular')

    def mostrar_estudiantes(self, obj):
        return ", ".join([e.nombre for e in obj.estudiantes.all()]) if obj.estudiantes.exists() else "Sin estudiantes"

    mostrar_estudiantes.short_description = "Estudiantes"


@admin.register(Madre)
class MadreAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'celular', 'mostrar_estudiantes')
    search_fields = ('nombre', 'celular')

    def mostrar_estudiantes(self, obj):
        return ", ".join([e.nombre for e in obj.estudiantes.all()]) if obj.estudiantes.exists() else "Sin estudiantes"

    mostrar_estudiantes.short_description = "Estudiantes"


@admin.register(Apoderado)
class ApoderadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'celular', 'mostrar_estudiantes')
    search_fields = ('nombre', 'celular')

    def mostrar_estudiantes(self, obj):
        return ", ".join([e.nombre for e in obj.estudiantes.all()]) if obj.estudiantes.exists() else "Sin estudiantes"

    mostrar_estudiantes.short_description = "Estudiantes"


@admin.register(Observacion)
class ObservacionAdmin(admin.ModelAdmin):
    list_display = ('get_estudiante', 'descripcion')
    search_fields = ('estudiante__nombre', 'descripcion')

    def get_estudiante(self, obj):
        return obj.estudiante.nombre if obj.estudiante else "Sin estudiante"

    get_estudiante.short_description = "Estudiante"


@admin.register(ReporteAlumno)
class ReporteAlumnoAdmin(admin.ModelAdmin):
    list_display = ('get_estudiante', 'condicion', 'get_padre',
                    'get_madre', 'get_apoderado', 'get_tutor', 'accion_respuesta', 'fecha')
    search_fields = ('estudiante__nombre', 'estudiante__dni', 'condicion')
    list_filter = ('condicion', 'tutor', 'accion_respuesta')

    def get_estudiante(self, obj):
        return f"{obj.estudiante.nombre} - {obj.estudiante.dni}" if obj.estudiante else "Sin estudiante"

    def get_padre(self, obj):
        return obj.padre.nombre if obj.padre else "No registrado"

    def get_madre(self, obj):
        return obj.madre.nombre if obj.madre else "No registrada"

    def get_apoderado(self, obj):
        return obj.apoderado.nombre if obj.apoderado else "No registrado"

    def get_tutor(self, obj):
        return f"{obj.tutor.nombre} {obj.tutor.apellido}" if obj.tutor else "No asignado"

    get_estudiante.short_description = "Estudiante"
    get_padre.short_description = "Padre"
    get_madre.short_description = "Madre"
    get_apoderado.short_description = "Apoderado"
    get_tutor.short_description = "Tutor"


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'grado',
                    'seccion', 'nombredeseccion')
    search_fields = ('nombre', 'apellido', 'grado', 'seccion')

    def nombredeseccion(self, obj):
        return obj.seccion.nombre if hasattr(obj.seccion, 'nombre') else "Sin nombre"

    nombredeseccion.short_description = "Nombre de la Sección"


@receiver(post_save, sender=ReporteAlumno)

def actualizar_historial_al_guardar_reporte(sender, instance, **kwargs):
    """Actualiza el historial del estudiante cada vez que se guarda un ReporteAlumno."""
    if instance.estudiante:
        historial, creado = HistorialAlumno.objects.get_or_create(estudiante=instance.estudiante)

        # Agregar el nuevo reporte al historial
        historial.reportes.add(instance)  

        # Contar correctamente todos los reportes asignados al historial
        historial.cantidad_reportes = historial.reportes.count()
        historial.save()

        print(f"Historial actualizado: {historial.cantidad_reportes} reportes para {instance.estudiante.nombre}")
