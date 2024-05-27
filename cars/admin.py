from django.contrib import admin
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value') # lista os campos para o grid do admin
    search_fields = ('model','brand') # Ao pesquisar um modelo/marca específico será feita a busca nos carros cadastrados

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)  # Registra as configurações
admin.site.register(Car, CarAdmin) 