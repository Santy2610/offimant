# Generated by Django 3.2.12 on 2024-03-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codificadores', '0006_trabajadores'),
    ]

    operations = [
        migrations.AddField(
            model_name='centrocosto',
            name='prod',
            field=models.CharField(default='No', max_length=2),
        ),
    ]