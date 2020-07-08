from django.db import models

from bases.models import ClaseModelo

class Proveedor(ClaseModelo):
    descripcion = models.CharField("Descripcion", max_length=100, unique=True)
    direccion = models.CharField("Direccion", max_length=250, null=True, blank=True)
    contacto = models.CharField("Contacto", max_length=100)
    telefono = models.CharField("Telefono", max_length=10, null=True, blank=True)
    email = models.CharField("Email", max_length=250,null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = "Proveedores"
