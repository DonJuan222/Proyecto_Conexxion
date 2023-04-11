from django import forms
from .models import Cliente,Factura


class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['ip','cedula','nombre','telefono_uno','telefonos_dos','valor_instalacion','fecha_instalacion','direccion',
                  'estado','descripcion','municipio','equipos','tipo_instalacion','cap_megas','ap']
        labels = {
        'ip': 'Ip del cliente',
        'cedula': 'Cedula del cliente',
        'nombre': 'Nombre y Apellido del cliente',
        'telefono_uno': 'Telefono del cliente',
        'telefonos_dos': 'Segundo telefono (Opcional)',
        'valor_instalacion': 'Valor de Instalacion',
        'fecha_instalacion': 'Fecha de instalacion del cliente',
        'direccion': 'Dirección',
        'descripcion': 'Detalles',
        'municipio': 'Municipio de Residencia',
        'equipos': 'Equipos',
        'tipo_instalacion': 'Tipo de Instalacion',
        'cap_megas': 'Megas contratadas',
        'ap': 'Conectado al Ap',
        
        }
        widgets = {
    
        'ip': forms.TextInput(attrs={'placeholder': 'Inserte la Ip del Cliente','id':'ip','class':'form-control'} ),
        'cedula': forms.TextInput(attrs={'placeholder': 'Inserte la cedula de identidad del cliente','id':'cedula','class':'form-control'} ),
        'nombre': forms.TextInput(attrs={'placeholder': 'Inserte el nombre del cliente','id':'nombre','class':'form-control'}),
        'telefono_uno': forms.TextInput(attrs={'class':'form-control','id':'telefono_uno','placeholder':'Telefono del cliente'}), 
        'telefonos_dos': forms.TextInput(attrs={'class':'form-control','id':'telefonos_dos','placeholder':'Segundo telefono del cliente'}),                                                                       
        'valor_instalacion': forms.TextInput(attrs={'class':'form-control','id':'valor_instalacion','placeholder':'Valor de Instalacion del cliente'}),                                                                                                     
        'fecha_instalacion':forms.DateInput(format=('%d-%m-%Y'),attrs={'id':'fecha_instalacion','class':'form-control','type':'date'} ),
        'direccion': forms.TextInput(attrs={'class':'form-control','id':'direccion','placeholder':'Direccion del cliente'}),                                                                       
        'descripcion': forms.TextInput(attrs={'class':'form-control','id':'descripcion','placeholder':'Direccion del cliente'}),
        
        'cap_megas': forms.TextInput(attrs={'class':'form-control','id':'cap_megas','placeholder':'Megas Contratadas'}),
        }

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['detalle','tipo_pago', 'valor_pago','n_recibo', 'fecha_pago', 'fecha_vencimiento']
        
        labels = {
        'detalle': 'Detalle',
        'valor_pago': 'Valor del Pago',
        'n_recibo': 'Numero de Recibo',
        'fecha_pago': 'Fecha de Pago',
        'fecha_vencimiento': 'Pago Valido Hasta',

        }
        widgets = {
    
        'fecha_pago': forms.DateInput(format=('%d-%m-%Y'),attrs={'id':'id_fecha_pago','class':'form-control','type':'date'} ),
        'n_recibo': forms.TextInput(attrs={'id':'id_n_recibo'}),
        'fecha_vencimiento': forms.DateInput(format=('%d-%m-%Y'),attrs={'id':'id_fecha_vencimiento','class':'form-control','type':'date'} ),

        }

        