# Generated by Django 3.2.8 on 2022-03-23 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_product', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('created_at',)},
        ),
    ]
