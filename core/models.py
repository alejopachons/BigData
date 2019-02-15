from django.db import models

# Create your models here.

class GetNumbers(models.Model):
    number1 = models.IntegerField(verbose_name="Número 1")
    number2 = models.IntegerField(verbose_name="Número 2")

    def suma(self):
        suma = self.number1 + self.number2
        return suma

    def resta(self):
        pass

    def potencia(self):
        pass

