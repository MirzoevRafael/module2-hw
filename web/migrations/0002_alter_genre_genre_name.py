# Generated by Django 5.0.3 on 2024-03-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]