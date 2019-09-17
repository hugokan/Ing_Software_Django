# Generated by Django 2.2.5 on 2019-09-17 00:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('telefono', models.CharField(max_length=50, verbose_name='Telefono')),
                ('email', models.CharField(max_length=80, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'nombre',
                'verbose_name_plural': 'nombres',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca')),
                ('descripcion', models.TextField()),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejercicio.Persona')),
            ],
            options={
                'verbose_name': 'titulo',
                'verbose_name_plural': 'titulos',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.CharField(max_length=50)),
                ('fecha_compra', models.DateTimeField(default=django.utils.timezone.now)),
                ('hora_compra', models.DateTimeField(blank=True, null=True)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejercicio.Persona')),
                ('titulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejercicio.Producto')),
            ],
        ),
    ]