# Generated by Django 4.0.3 on 2022-03-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='opis',
            field=models.TextField(default=''),
        ),
    ]
