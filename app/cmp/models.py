from django.db import models

from bases.models import ClaseModelo
from inv.models import Producto

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


class ComprasEnc(ClaseModelo):
    fecha_compra = models.DateField(null=True, blank=True)
    observaciones = models.TextField(blank=True, null=True)
    no_factura = models.CharField(max_length=100)
    fecha_factura = models.DateField()
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.observaciones)

    def save(self):
        self.observaciones = self.observaciones.upper()
        self.total = self.sub_total - self.descuento
        super(ComprasEnc, self).save()

    class Meta:
        verbose_name_plural = "Encabezado Compras"
        verbose_name = "Encabezado Compra"


class ComprasDet(ClaseModelo):
    compra = models.ForeignKey(ComprasEnc, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio_prv = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    costo = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad))*float(self.precio_prv))
        self.total = self.sub_total-float(self.descuento)
        super(ComprasDet,self).save()

    class Meta:
        verbose_name_plural = "Detalles Compras"
        verbose_name = "Detalle Compra"