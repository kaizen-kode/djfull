# Generated by Django 2.2 on 2020-07-04 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_Creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('fecha_Modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificacion')),
                ('usuario_Modifica', models.IntegerField(blank=True, null=True, verbose_name='Usuario Modifica')),
                ('descripcion', models.CharField(help_text='Descripcion de la categoria', max_length=100, unique=True, verbose_name='Descripcion')),
                ('usuario_Crea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
