from django.db import models

# Create your models here.

class Pacientes(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.nome