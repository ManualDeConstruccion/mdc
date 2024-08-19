import json
from django.db import migrations

def cargar_permisos(apps, schema_editor):
    PermitType = apps.get_model('architecture_projects', 'PermitType')
    PermitGroup = apps.get_model('architecture_projects', 'PermitGroup')
    PermitSubType = apps.get_model('architecture_projects', 'PermitSubType')

    # Cambia la ruta si es necesario
    with open('applications/architecture_projects/data/permissions_minvu.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for permiso in data['permissions']:
        pt = PermitType.objects.create(permit_type=permiso["permit_type"])
        for grupo in permiso["permit_groups"]:
            pg = PermitGroup.objects.create(permit_type=pt, permit_group=grupo["group_name"])
            for subtype in grupo["subtypes"]:
                PermitSubType.objects.create(permit_group=pg, permit_sub_type=subtype)


class Migration(migrations.Migration):

    dependencies = [
        ('architecture_projects', '0007_permitgroup_permittype_and_more'),
    ]

    operations = [
        migrations.RunPython(cargar_permisos),
    ]
