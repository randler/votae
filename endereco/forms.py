from django import forms

from .models import Endereco


class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = '__all__'

