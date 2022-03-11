# Generated by Django 3.2.8 on 2022-03-11 07:16

from django.db import migrations

from api_account.contants import RoleData


def initial_role_data(apps, schema_editor):
    role_model = apps.get_model("api_account", "Role")

    roles = []

    for role in RoleData:
        roles.append(role_model(id=role.value['id'], name=role.value['name']))

    role_model.objects.bulk_create(roles)


def delete_all_data(apps, schema_editor):
    role_model = apps.get_model("api_account", "Role")
    role_model.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api_account', '0002_alter_account_role'),
    ]

    operations = [
        migrations.RunPython(initial_role_data, delete_all_data)
    ]
