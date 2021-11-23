from django.db import models


# Create your models here.

class Gasto(models.Model):
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateField(null=True, blank=True)


