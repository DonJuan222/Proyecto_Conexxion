from django.urls import path
from . import views
from .views import crear_factura


urlpatterns = [

    path('listarClientes', views.ListarClientes.as_view(), name='listarClientes'),
    path('agregarCliente', views.AgregarCliente.as_view(), name='agregarCliente'),
    # path('importarClientes', import_clientes, name='importarClientes'),
    # path('exportarClientes', views.ExportarClientes.as_view(), name='exportarClientes'),
    path('editarCliente/<int:p>', views.EditarCliente.as_view(), name='editarCliente'),
    path('eliminar/<str:modo>/<int:p>', views.Eliminar.as_view(), name='eliminar'),
        
    path('listarFactura/<int:factura_id>/', views.ListarFactura.as_view(), name='listarFactura'),
    path('crear_factura/<int:cliente_id>/',crear_factura , name='crear_factura'),
    path('verFactura/<int:p>',views.VerFactura.as_view(), name='verFactura'),
    # path('generarFacturaPDF/<int:p>',views.GenerarFacturaPDF.as_view(), name='generarFacturaPDF'),
    path('listarClientesRetirados', views.ListarClientesRetirados.as_view(), name='listarClientesRetirados'),


]

