# Generated by Django 3.2.12 on 2024-02-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codificadores', '0005_causas'),
    ]

    operations = [
        migrations.CreateModel(
            name='trabajadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
    ]
