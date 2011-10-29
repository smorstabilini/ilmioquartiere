# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

REQUEST_TYPE = (
    (1, 'Richiesta'),
    (2, 'Offerta'),
)

WHEN = (
    (1, 'Mattina'),
    (2, 'Pomeriggio'),
    (3, 'Sera'),
)

COST = (
    (1, 'Gratis'),
    (2, 'Scambio'),
    (3, 'Pagamento'),
)

class ReqOff(models.Model):
    creator = models.ForeignKey(
        User,
        unique=True,
    )

    description = models.CharField(
        max_length=100,
        verbose_name='Inserisci la tua richiesta',
    )
    when = models.IntegerField(
        choices=WHEN,
    )

    mon = models.BooleanField(verbose_name='Lunedì')
    tue = models.BooleanField(verbose_name='Martedì')
    wed = models.BooleanField(verbose_name='Mercoledì')
    thu = models.BooleanField(verbose_name='Giovedì')
    fri = models.BooleanField(verbose_name='Venerdì')
    sat = models.BooleanField(verbose_name='Sabato')
    sun = models.BooleanField(verbose_name='Domenica')


class Discrict(models.Model):
    coutry = models.CharField(
        max_length=2
    )
    state = models.CharField(
        max_length=2,
    )
    city = models.CharField(
        max_length=30,
    )
    name = models.CharField(
        max_length=30,
    )
