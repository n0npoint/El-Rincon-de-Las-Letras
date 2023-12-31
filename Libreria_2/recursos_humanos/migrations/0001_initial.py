# Generated by Django 4.2.4 on 2023-08-19 02:21

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
            name='TbDepartamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Departamento')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre Departamento')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'db_table': 'tb_departamento',
            },
        ),
        migrations.CreateModel(
            name='TbProfesion',
            fields=[
                ('id_cargo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Cargo')),
                ('nombre_cargo', models.CharField(max_length=45, unique=True, verbose_name='Nombre Profesion')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Profesion',
                'verbose_name_plural': 'Profesiones',
                'db_table': 'tb_profesion',
            },
        ),
        migrations.CreateModel(
            name='TbEmpleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Empleado')),
                ('dni', models.CharField(max_length=20, unique=True, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('fecha_nacimiento', models.DateTimeField(verbose_name='Fecha Nacimiento')),
                ('numero_telefono', models.CharField(max_length=20, unique=True, verbose_name='Número de Teléfono')),
                ('numero_celular', models.CharField(max_length=20, unique=True, verbose_name='Número de Celular')),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='Email')),
                ('fecha_contratacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Contratación')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='empleados', verbose_name='Foto')),
                ('id_cargo', models.OneToOneField(db_column='id_cargo', on_delete=django.db.models.deletion.DO_NOTHING, to='recursos_humanos.tbprofesion', verbose_name='ID Cargo')),
                ('id_departamento', models.ForeignKey(db_column='id_departamento', on_delete=django.db.models.deletion.DO_NOTHING, to='recursos_humanos.tbdepartamento', verbose_name='ID Departamento')),
                ('username', models.OneToOneField(db_column='username', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'tb_empleado',
            },
        ),
    ]
