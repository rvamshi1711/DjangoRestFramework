# Generated by Django 3.1.5 on 2021-02-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
