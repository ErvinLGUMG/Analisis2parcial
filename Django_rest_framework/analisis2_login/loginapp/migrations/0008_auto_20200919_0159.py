# Generated by Django 3.0.8 on 2020-09-19 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0007_auto_20200919_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dormitorio',
            name='residente',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='consejero',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
