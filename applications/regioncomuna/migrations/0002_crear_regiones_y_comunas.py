from django.db import migrations
import os
import json


def cargar_datos_regioncomuna(apps, schema_editor):
    Region = apps.get_model('regioncomuna', 'Region')
    Comuna = apps.get_model('regioncomuna', 'Comuna')

    # Construye la ruta al archivo JSON
    current_file = os.path.dirname(__file__)
    json_path = os.path.join(current_file, '..', 'data', 'regioncomuna.json')

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

        for region_data in data['regiones']:
            region, created = Region.objects.get_or_create(
                region=region_data['region']
            )
            for comuna_data in region_data['comunas']:
                Comuna.objects.create(comuna=comuna_data, region=region)


class Migration(migrations.Migration):

    dependencies = [
        ('regioncomuna', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_datos_regioncomuna),
    ]
