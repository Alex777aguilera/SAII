from django.db import models

class Puesto(models.Model):
    descripcion_puesto = models.CharField(max_length = 25, null = False, blank = False)
    def __str__(self):
        return f'{self.pk,self.descripcion_puesto}'

class Postulante(models.Model):
    primer_nombre = models.CharField(max_length = 50, null = False, blank = False)
    primer_apellido = models.CharField(max_length = 50, null = False, blank = False)
    correo = models.CharField(max_length = 50, null = True, blank = True)
    telefono_cel = models.CharField(max_length = 50, null = False, blank = False)
    edad = models.IntegerField()
    residencia = models.CharField(max_length = 50, null = False, blank = False)
    fecha_registro = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'{self.pk,self.primer_nombre+" "+self.primer_apellido}'

class Vacante(models.Model):
    puesto = models.ForeignKey(Puesto,on_delete=models.CASCADE, null = False, blank = False)
    descripcion_vacante = models.CharField(max_length = 200, null = False, blank = False)
    requisitos = models.CharField(max_length = 200, null = False, blank = False)
    cantidad_vacantes = models.IntegerField()
    fecha_expira = models.DateField(auto_now = False, auto_now_add = False)
    fecha_registro = models.DateField(auto_now_add = True)

class Solicitud_vacante(models.Model):
    vacante = models.ForeignKey(Vacante,on_delete=models.CASCADE, null = False, blank = False)
    postulante = models.ForeignKey(Postulante,on_delete=models.CASCADE, null = False, blank = False)
    fecha_solicitud = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'{self.pk,self.vacante.puesto.descripcion_puesto,self.vacante.descripcion_vacante,self.vacante.fecha_expira,self.postulante.primer_nombre,self.postulante.primer_apellido,self.fecha_solicitud}'
