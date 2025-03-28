from django.db import models
from django.utils.timezone import now


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, blank=True, null=True, unique=True)
    grado = models.CharField(max_length=1)
    seccion = models.CharField(max_length=1, blank=True)
    nombredeseccion = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.grado} -{self.seccion} - {self.nombredeseccion} "


class Tutor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    apellido = models.CharField(max_length=100, unique=True)
    grado = models.CharField(max_length=1)
    seccion = models.CharField(max_length=15, blank=True)

    class Meta:
        verbose_name = "Tutor"
        verbose_name_plural = "Tutores"

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"


class Padre(models.Model):
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=15, blank=True, null=True)
    estudiantes = models.ManyToManyField(
        'Estudiante', related_name='padres', blank=True)

    def __str__(self):
        return f"{self.nombre}"


class Madre(models.Model):
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=15, blank=True, null=True)
    estudiantes = models.ManyToManyField(
        'Estudiante', related_name='madres', blank=True)

    def __str__(self):
        return f"{self.nombre}"


class Apoderado(models.Model):
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=15, blank=True)
    estudiantes = models.ManyToManyField(
        'Estudiante', related_name='apoderados', blank=True)

    def __str__(self):
        return f"{self.nombre}"


class Observacion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"Observación de {self.estudiante.nombre if self.estudiante else 'Sin estudiante'}"


class AccionRespuesta(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"


class ReporteAlumno(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    padre = models.ForeignKey(
        Padre, on_delete=models.SET_NULL, null=True, blank=True)
    madre = models.ForeignKey(
        Madre, on_delete=models.SET_NULL, null=True, blank=True)
    apoderado = models.ForeignKey(
        Apoderado, on_delete=models.SET_NULL, null=True, blank=True)
    condicion = models.CharField(
        max_length=255,
        choices=[
            ("embarazo", "Embarazo"),
            ("madre_lactante", "Madre Lactante"),
            ("tratamiento_psiquiatrico", "Tratamiento Psiquiátrico"),
            ("certificado_medico", "Certificado Médico"),
            ("sustancias_psicoactivas", "Sustancias Psicoactivas"),
            ("evade_clases", "Evade Clases"),
            ("alcohol", "Consume Alcohol"),
            ("violencia", "Violencia"),
            ("siseve", "SISEVE"),
            ("tocamientos_indebidos", "Tocamientos Indebidos")
        ]
    )
    accion_respuesta = models.ForeignKey(
        AccionRespuesta, on_delete=models.SET_NULL, null=True, blank=True)
    tutor = models.ForeignKey(
        Tutor, on_delete=models.SET_NULL, null=True, blank=True)
    observacion = models.ForeignKey(Observacion, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Guarda el reporte primero

        if self.padre:
            self.padre.estudiantes.add(self.estudiante)  # Asocia el estudiante al padre
            self.padre.save()  # Guarda cambios en el padre

        if self.madre:
            self.madre.estudiantes.add(self.estudiante)  # Asocia el estudiante a la madre
            self.madre.save()  # Guarda cambios en la madre

        if self.apoderado:
            self.apoderado.estudiantes.add(self.estudiante)  # Asocia el estudiante al apoderado
            self.apoderado.save()  # Guarda cambios en el apoderado

        # Asocia el estudiante a la acción de respuesta
        if self.accion_respuesta and self.accion_respuesta.estudiante is None:
            self.accion_respuesta.estudiante = self.estudiante
            self.accion_respuesta.save()

        # Asocia el estudiante a todas las observaciones
        if self.observacion:  # Verifica si existe una observación
            if self.observacion.estudiante is None:
                self.observacion.estudiante = self.estudiante
                self.observacion.save()


    def __str__(self):
        return f"Reporte de {self.estudiante} - {self.condicion} - {self.fecha.strftime('%d/%m/%Y %H:%M:%S')}"


class HistorialAlumno(models.Model):
    estudiante = models.OneToOneField(
        Estudiante, on_delete=models.CASCADE, related_name='historial')
    reportes = models.ManyToManyField(ReporteAlumno, blank=True)
    fecha = models.DateTimeField(default=now)

    def actualizar_historial(self):
        """ Obtiene todos los reportes del estudiante y los agrega al historial """
        reportes_del_estudiante = ReporteAlumno.objects.filter(
            estudiante=self.estudiante)
        # Agregar todos los reportes
        self.reportes.set(reportes_del_estudiante)
        self.save()

    def __str__(self):
        return f"Historial de {self.estudiante} - {self.fecha.strftime('%d/%m/%Y %H:%M:%S')}"
