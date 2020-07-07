# Generated by Django 2.2 on 2020-07-07 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0004_unidadmedida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_Creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('fecha_Modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificacion')),
                ('usuario_Modifica', models.IntegerField(blank=True, null=True, verbose_name='Usuario Modifica')),
                ('codigo', models.CharField(max_length=20, unique=True, verbose_name='Codigo')),
                ('codigo_barra', models.CharField(max_length=50, unique=True, verbose_name='Codigo Barra')),
                ('descripcion', models.CharField(help_text='Descripcion del Producto', max_length=200, unique=True, verbose_name='Descripcion')),
                ('precio', models.FloatField(default=0, max_length=15, verbose_name='Precio')),
                ('existencia', models.IntegerField(default=0, verbose_name='Existencia')),
                ('ultima_compra', models.DateTimeField(blank=True, null=True, verbose_name='Ultima Compra')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.Marca')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.SubCategoria')),
                ('unidadmedida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.UnidadMedida')),
                ('usuario_Crea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'unique_together': {('codigo', 'codigo_barra')},
            },
        ),
    ]