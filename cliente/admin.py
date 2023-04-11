from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Cliente, Factura, Municipio, Equipos, Detalle,Tipo_Instalacion,ClienteRetirado,FacturaRetirada,Ap,Tecnico

# Register your models here.

class ClienteResource(resources.ModelResource):
    class Meta:
        model=Cliente

class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('ip','cedula','nombre','telefono_uno','telefonos_dos','valor_instalacion','fecha_instalacion','direccion',
                  'estado','descripcion','municipio','equipos','tipo_instalacion','cap_megas','ap')
    resource_class=ClienteResource

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Factura)
admin.site.register(Municipio)
admin.site.register(Equipos)
admin.site.register(Detalle)
admin.site.register(Tipo_Instalacion)
admin.site.register(ClienteRetirado)
admin.site.register(FacturaRetirada)
admin.site.register(Ap)
admin.site.register(Tecnico)