from django.db import models

from bases.models import ClaseModelo

# Create your models here.

class Categoria(ClaseModelo):
    descripcion = models.CharField("Descripcion", max_length=100, help_text="Descripcion de la categoria", unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria,self).save()

    class Meta:
        verbose_name_plural = "Categorias"


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField("Descripcion", max_length=100, help_text="Descripcion de la sub categoria", unique=True)

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)


    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria,self).save()

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria', 'descripcion')


class Marca(ClaseModelo):
    descripcion = models.CharField("Descripcion", max_length=100, help_text="Descripcion de la marca", unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca,self).save()

    class Meta:
        verbose_name_plural = "Marcas"        


class UnidadMedida(ClaseModelo):
    descripcion = models.CharField("Descripcion", max_length=100, help_text="Descripcion de la Unidad de Medida", unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida,self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medida"        


class Producto(ClaseModelo):
    codigo = models.CharField("Codigo", max_length=20, null=False, unique=True)
    codigo_barra = models.CharField("Codigo Barra", max_length=50, null=False, unique=True)
    descripcion = models.CharField("Descripcion", max_length=200, help_text="Descripcion del Producto", unique=True, null=False)
    precio = models.FloatField("Precio", max_length=15, default=0)
    existencia = models.IntegerField("Existencia", default=0)
    ultima_compra = models.DateTimeField("Ultima Compra", null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    unidadmedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)

    

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto,self).save()

    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo', 'codigo_barra')        
