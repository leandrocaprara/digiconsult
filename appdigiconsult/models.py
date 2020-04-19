from django.db import models

# Create your models here.

class Pacientes(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=True, verbose_name=u'Nome')
    cpf = models.CharField(max_length=11, blank=False, null=True, verbose_name=u'CPF')

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.nome