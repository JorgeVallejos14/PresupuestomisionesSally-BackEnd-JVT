from django.contrib import admin
from .models import Mision, Gasto

# Register your models here.
@admin.register(Mision)
class MisionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lider', 'zona', 'activa')
    list_filter = ('activa', 'zona')
    search_fields = ('nombre', 'lider')


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('concepto', 'mision', 'categoria', 'registrado', 'monto_clp')
    list_filter = ('categoria', 'mision')
    search_fields = ('concepto',)

    @admin.display(description='Monto', ordering='monto')
    def monto_clp(self, obj):
        return f"${obj.monto:,}".replace(",", ".")