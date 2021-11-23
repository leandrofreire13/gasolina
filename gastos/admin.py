from django.contrib import admin

from .models import Gasto


# Register your models here.

class GastoCampos(admin.ModelAdmin):
    list_display = ('valor', 'data')


admin.site.register(Gasto, GastoCampos)
