from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from . import models

class PacientesAdd(forms.ModelForm):
    class Meta:
        model = models.Pacientes
        fields = ['nome', 'cpf']



    # nome = forms.CharField(help_text="Insira o nome do paciente.")
    # cpf = forms.CharField(max_length=11)

    # def clean_fields(self):
    #     nome = self.cleaned_data['nome']
    #     cpf = self.cleaned_data['cpf']

    #     if cpf.len(s) < 11:
    #         raise ValidationError(_('CPF inválido'))

    #     return nome, cpf
