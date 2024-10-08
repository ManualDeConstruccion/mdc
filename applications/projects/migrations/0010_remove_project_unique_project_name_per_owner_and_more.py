# Generated by Django 5.0.7 on 2024-08-18 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_remove_project_unique_project_name_per_owner_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='project',
            name='unique_project_name_per_owner',
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=100, verbose_name='Nombre del proyecto'),
        ),
    ]
