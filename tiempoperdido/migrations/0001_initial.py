# Generated by Django 3.2.12 on 2024-06-01 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tiempo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
                ('equipo', models.CharField(max_length=150)),
                ('fechaI', models.DateField()),
                ('fechaF', models.DateField()),
                ('causa', models.CharField(max_length=200)),
                ('observacion', models.TextField()),
            ],
        ),
    ]
