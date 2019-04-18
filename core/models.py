from django.db import models


class Numero(models.Model):
    numero = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.numero
