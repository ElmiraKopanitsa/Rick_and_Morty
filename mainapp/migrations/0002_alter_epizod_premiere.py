# Generated by Django 4.1.5 on 2023-01-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epizod',
            name='premiere',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
