# Generated by Django 3.0.8 on 2020-09-19 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0006_dormitorio_programa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userumg',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
