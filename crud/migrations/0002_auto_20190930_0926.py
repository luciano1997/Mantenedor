# Generated by Django 2.2.3 on 2019-09-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
