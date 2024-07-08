# Generated by Django 4.2.2 on 2024-07-07 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creador'),
            preserve_default=False,
        ),
    ]
