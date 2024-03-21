from django.contrib import admin
from django.contrib import admin
from .models import miModelo

# Register your models here.
admin.site.register(miModelo)

# Register your models here.
class miModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'email')