# Generated by Django 3.2.12 on 2024-04-09 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0005_auto_20240408_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantplan',
            name='abrilR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantplan',
            name='agostoR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantplan',
            name='diciembreR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantplan',
            name='eneroR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantplan',
            name='febreroR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantplan',
            name='julioR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantplan',
            name='junioR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantplan',
            name='marzoR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantplan',
            name='mayoR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantplan',
            name='noviembreR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantplan',
            name='octubreR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mantplan',
            name='septiembreR',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
