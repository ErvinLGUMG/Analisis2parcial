# Generated by Django 3.0.8 on 2020-07-31 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_auto_20200731_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userumg',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
