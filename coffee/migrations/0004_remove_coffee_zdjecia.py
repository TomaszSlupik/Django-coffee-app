# Generated by Django 4.0.1 on 2022-03-13 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_coffee_zdjecia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='zdjecia',
        ),
    ]
