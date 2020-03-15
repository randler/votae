from django.contrib import admin
from .models import Voto

# Register your models here.


class VotoAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'endereco')


admin.site.register(Voto, VotoAdmin)
