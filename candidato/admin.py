from django.contrib import admin
from .models import Candidato

# Register your models here.


class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco')


admin.site.register(Candidato, CandidatoAdmin)
