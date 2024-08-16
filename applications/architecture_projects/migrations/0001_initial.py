# Generated by Django 5.0.7 on 2024-08-16 03:57

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0007_alter_project_name'),
        ('regioncomuna', '0002_crear_regiones_y_comunas'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchitectureProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('architecture_project_name', models.CharField(error_messages={'unique': 'Este nombre de proyecto ya existe. Debes escoger otro.'}, max_length=100, unique=True, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Descripción')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Fecha de inicio')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='architecture_projects', to='projects.project', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='ObraNueva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('numero_solicitud', models.IntegerField(blank=True, null=True, verbose_name='Número de solicitud')),
                ('fecha_ingreso', models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso')),
                ('codigo_rpi', models.CharField(blank=True, max_length=100, null=True, verbose_name='Código Registro Proyectos Inmobiliarios')),
                ('alteracion', models.BooleanField(default=False, verbose_name='Alteración')),
                ('cambio_destino', models.BooleanField(default=False, verbose_name='Cambio de destino')),
                ('demolicion', models.BooleanField(default=False, verbose_name='Demolición')),
                ('project_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre del proyecto')),
                ('numero_CIP', models.CharField(blank=True, max_length=100, null=True, verbose_name='Número Certificado de Informaciones Previas')),
                ('fecha_CIP', models.DateField(blank=True, null=True, verbose_name='Fecha Certificado de Informaciones Previas')),
                ('calculista', models.BooleanField(default=False, verbose_name='Calculista')),
                ('constructor', models.BooleanField(default=False, verbose_name='Constructor')),
                ('inspector_tecnico', models.BooleanField(default=False, verbose_name='Inspector Técnico de Obra')),
                ('revisor_independiente', models.BooleanField(default=False, verbose_name='Revisor Independiente')),
                ('revisor_calculo', models.BooleanField(default=False, verbose_name='Revisor de Proyecto de Cálculo Estructural')),
                ('loteo_contruccion_simultanea', models.BooleanField(blank=True, default=None, null=True, verbose_name='Loteo con construcción simultánea')),
                ('loteo_dfl2', models.BooleanField(blank=True, default=None, null=True, verbose_name='Loteo DFL2')),
                ('architecture_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='architecture_type', to='architecture_projects.architectureproject', verbose_name='Proyecto de arquitectura')),
                ('comuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='architecture_type', to='regioncomuna.comuna', verbose_name='Comuna')),
            ],
            options={
                'verbose_name': 'Permiso de Edificación - Obra Nueva',
            },
        ),
    ]
