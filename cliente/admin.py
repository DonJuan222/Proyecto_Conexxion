from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Cliente, Factura, Municipio, Equipos, Capacidad_Megas, Detalle, Tipo_Instalacion, Tipo_Pago

# Register your models here.

class ClienteResource(resources.ModelResource):
    class Meta:
        model=Cliente


class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('ip','cedula','nombre','apellido','telefono_uno','telefonos_dos','mensualidad','fecha_instalacion','direccion',
                  'tipo_instalacion','status','descripcion')
    resource_class=ClienteResource

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Factura)
admin.site.register(Municipio)
admin.site.register(Equipos)
admin.site.register(Capacidad_Megas)
admin.site.register(Detalle)
admin.site.register(Tipo_Instalacion)
admin.site.register(Tipo_Pago)

