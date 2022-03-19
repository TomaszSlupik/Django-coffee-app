from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from random import choices
from django.db import models

class Coffee (models.Model):
    name = models.CharField (max_length=20)
    description = models.TextField (default='')
    type_all = (
        ('ARABICA', 'ARABICA'),
        ('KAWA MIESZANA','KAWA MIESZANA'),
        ('ROBUSTA', 'ROBUSTA'),
    )   
    typecoffee = models.CharField (max_length=13, choices=type_all)
    zdjecia =models.ImageField(upload_to='zdjecia', null=True, blank=True)

    




