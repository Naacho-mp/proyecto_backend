# Generated by Django 5.2.1 on 2025-05-28 20:29

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_digital', '0003_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[500, 300], upload_to='mostrar_productos/'),
        ),
    ]
