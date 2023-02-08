from django import forms
from .models import Cliente,Factura


class ClienteFormulario(forms.ModelForm):
    # tipoInsta =  [ ('------','------'),('Fibra Optica','Fibra'),('Radio Enlace','Radio')]

    # tipo_instalacion = forms.CharField(
    #     label="Tipo de Instalacion",
    #     max_length=20,
    #     widget=forms.Select(choices=tipoInsta,attrs={'placeholder': 'Tipo de Instalacion',
    #     'id':'tipo_instalacion','class':'form-control'}
    #     )
    #     )

    class Meta:
        model = Cliente
        fields = ['ip','cedula','nombre','apellido','telefono_uno','telefonos_dos','mensualidad','fecha_instalacion','direccion',
                  'estado','descripcion','municipio','equipos','tipo_instalacion','cap_megas']
        labels = {
        'ip': 'Ip del cliente',
        'cedula': 'Cedula del cliente',
        'nombre': 'Nombre del cliente',
        'apellido': 'Apellido del cliente',
        'telefono_uno': 'Telefono del cliente',
        'telefonos_dos': 'Segundo telefono (Opcional)',
        'mensualidad': 'Mensualidad cliente',
        'fecha_instalacion': 'Fecha de instalacion del cliente',
        'direccion': 'Dirección',
        'estado': 'Estado del Cliente',
        'descripcion': 'Detalles',
        'municipio': 'Municipio',
        'equipos': 'Equipos o Estado',
        'tipo_instalacion': 'Tipo de Instalacion',
        'cap_megas': 'Capacidad de Megas',
        }
        widgets = {
    
        'ip': forms.TextInput(attrs={'placeholder': 'Inserte la Ip del Cliente','id':'ip','class':'form-control'} ),
        'cedula': forms.TextInput(attrs={'placeholder': 'Inserte la cedula de identidad del cliente','id':'cedula','class':'form-control'} ),
        'nombre': forms.TextInput(attrs={'placeholder': 'Inserte el nombre del cliente','id':'nombre','class':'form-control'}),
        'apellido': forms.TextInput(attrs={'class':'form-control','id':'apellido','placeholder':'El apellido del cliente'}),
        'telefono_uno': forms.TextInput(attrs={'class':'form-control','id':'telefono_uno','placeholder':'Telefono del cliente'}), 
        'telefonos_dos': forms.TextInput(attrs={'class':'form-control','id':'telefonos_dos','placeholder':'Segundo telefono del cliente'}),                                                                       
        'mensualidad': forms.TextInput(attrs={'class':'form-control','id':'mensualidad','placeholder':'Mensualidad del cliente'}),                                                                                                     
        'fecha_instalacion':forms.DateInput(format=('%d-%m-%Y'),attrs={'id':'fecha_instalacion','class':'form-control','type':'date'} ),
        'direccion': forms.TextInput(attrs={'class':'form-control','id':'direccion','placeholder':'Direccion del cliente'}),                                                                       
        'tipo_instalacion': forms.TextInput(attrs={'class':'form-control','id':'tipo_instalacion','placeholder':'Tipo de instalacion'}),                                                                       
        'descripcion': forms.TextInput(attrs={'class':'form-control','id':'descripcion','placeholder':'Descripcion'}), 
           
        }

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['detalle','tipo_pago', 'valor_pago', 'fecha_pago', 'fecha_vencimiento']
        
        labels = {
        'detalle': 'Detalle',
        'valor_pago': 'Valor del Pago',
        'fecha_pago': 'Fecha de Pago',
        'fecha_vencimiento': 'Pago Valido Hasta',

        }
        widgets = {
    
        'descripcion': forms.TextInput(attrs={'placeholder': 'Inserte el detalle de la factura','id':'ip','class':'form-control'} ),
        'valor_pago': forms.TextInput(attrs={'placeholder': 'Inserte el valor de pago','id':'cedula','class':'form-control'} ),
        'fecha_pago': forms.DateInput(format=('%d-%m-%Y'),attrs={'id':'fecha_pago','class':'form-control','type':'date'} ),
        'fecha_vencimiento': forms.DateInput(format=('%d-%m-%Y'),attrs={'id':'fecha_vencimiento','class':'form-control','type':'date'} ),

        }

        