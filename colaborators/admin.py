from django.contrib import admin
from .models import Colaborator
# Register your models here.

class ColaboratorAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
admin.site.register(Colaborator, ColaboratorAdmin)