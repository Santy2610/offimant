# Generated by Django 3.2.12 on 2024-03-11 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producciones', '0003_materiales_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materiales',
            name='fecha',
        ),
    ]
