# Generated by Django 3.2.12 on 2024-03-13 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producciones', '0005_materiales_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='producciones',
            name='fechaf',
            field=models.DateField(default='2024-03-12'),
            preserve_default=False,
        ),
    ]