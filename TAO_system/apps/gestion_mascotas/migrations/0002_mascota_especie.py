# Generated by Django 3.1.2 on 2020-10-11 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='especie',
            field=models.CharField(max_length=50, null=True),
        ),
    ]