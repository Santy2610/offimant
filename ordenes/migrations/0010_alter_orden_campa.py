# Generated by Django 3.2.12 on 2024-03-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0009_orden_campa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='campa',
            field=models.CharField(max_length=7, null=True),
        ),
    ]