from django.contrib import admin
from .models import Endereco

# Register your models here.


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'cidade', 'cidade_id', 'estado', 'estado_id')


admin.site.register(Endereco, EnderecoAdmin)
