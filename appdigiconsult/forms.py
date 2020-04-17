from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class PacientesAdd(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PacientesAdd, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'bmd-label-floating'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class = 'form-group bmd-form-group'),
                Column('cpf', css_class = 'form-group bmd-form-group'),
            ),
            Submit('submit', 'Enviar'),
        )
        



    # nome = forms.CharField(help_text="Insira o nome do paciente.")
    # cpf = forms.CharField(max_length=11)

    # def clean_fields(self):
    #     nome = self.cleaned_data['nome']
    #     cpf = self.cleaned_data['cpf']

    #     if cpf.len(s) < 11:
    #         raise ValidationError(_('CPF inválido'))

    #     return nome, cpf
