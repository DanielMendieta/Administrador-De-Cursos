from django.contrib import admin
from .models import cursos, Docente

# Register your models here.
#admin.site.register(cursos)

@admin.register(cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creditos')
    search_fields = ('nombre',)
    list_per_page = 10

admin.site.register(Docente)


