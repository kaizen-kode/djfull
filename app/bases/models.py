from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClaseModelo(models.Model):
    estado = models.BooleanField("Estado", default=True)
    fecha_Creacion = models.DateTimeField("Fecha Creacion", auto_now_add= True)
    fecha_Modificado = models.DateTimeField("Fecha Modificacion", auto_now=True)
    usuario_Crea = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_Modifica = models.IntegerField("Usuario Modifica", null=True, blank=True)

    class Meta:
        abstract=True 