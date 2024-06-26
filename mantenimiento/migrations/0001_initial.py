# Generated by Django 3.2.12 on 2024-04-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mantplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=150)),
                ('equipo', models.CharField(max_length=150)),
                ('tarea', models.TextField()),
                ('eneroP', models.BooleanField()),
                ('febreroP', models.BooleanField()),
                ('marzoP', models.BooleanField()),
                ('abrilP', models.BooleanField()),
                ('mayoP', models.BooleanField()),
                ('junioP', models.BooleanField()),
                ('julioP', models.BooleanField()),
                ('agostoP', models.BooleanField()),
                ('septiembreP', models.BooleanField()),
                ('octubreP', models.BooleanField()),
                ('noviembreP', models.BooleanField()),
                ('diciembreP', models.BooleanField()),
                ('eneroR', models.BooleanField()),
                ('febreroR', models.BooleanField()),
                ('marzoR', models.BooleanField()),
                ('abrilR', models.BooleanField()),
                ('mayoR', models.BooleanField()),
                ('junioR', models.BooleanField()),
                ('julioR', models.BooleanField()),
                ('agostoR', models.BooleanField()),
                ('septiembreR', models.BooleanField()),
                ('octubreR', models.BooleanField()),
                ('noviembreR', models.BooleanField()),
                ('diciembreR', models.BooleanField()),
            ],
        ),
    ]
