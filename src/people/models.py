from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta: db_table = "personas"

    def _str_(self):
        return f'{self.nombres} {self.apellidos} {self.email}'
