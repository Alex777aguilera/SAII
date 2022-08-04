from django.db import models



class Desarrolladores(models.Model):
    primer_nombre = models.CharField(max_length = 50, null = False, blank = False)
    primer_apellido = models.CharField(max_length = 50, null = False, blank = False)
    correo = models.CharField(max_length = 50, null = True, blank = True)
    campus = models.CharField(max_length = 50, null = False, blank = False)
    

    def __str__(self):
        return f'{self.pk,self.primer_nombre+" "+self.primer_apellido}'

