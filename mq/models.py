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

class Richiesta(models.Model):
    """
    Richiesta.
    """
    creator = models.ForeignKey(User)
    description = models.CharField(
        max_length=500,
        verbose_name='Inserisci la tua richiesta',
    )
    when = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)


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

"""
class Abilita(models.Model):
    # tag: 1 o 2 parole
    short = models.CharField(max_length=50)

    # descrizione lunga
    descrizione = models.CharField(max_length=200)

    class Meta:
        verbose_name = "abilità"
        verbose_name_plural = "abilita"
"""

