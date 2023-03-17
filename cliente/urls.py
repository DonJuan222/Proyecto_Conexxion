from django.urls import path
from . import views
from .views import crear_factura


urlpatterns = [

    path('listarClientes', views.ListarClientes.as_view(), name='listarClientes'),
    path('cambiar_estado/<int:cliente_id>/', views.ListarClientes.as_view(), name='cambiar_estado_cliente'),
    path('agregarCliente', views.AgregarCliente.as_view(), name='agregarCliente'),
    # path('importarClientes', import_clientes, name='importarClientes'),
    # path('exportarClientes', views.ExportarClientes.as_view(), name='exportarClientes'),
    path('editarCliente/<int:p>', views.EditarCliente.as_view(), name='editarCliente'),
    path('eliminar/<str:modo>/<int:p>', views.Eliminar.as_view(), name='eliminar'),
    path('eliminar_retirado/<str:modo>/<int:p>', views.EliminarClienteRetirado.as_view(), name='eliminar'),
        
    path('listarFactura/<int:cliente_id>/', views.ListarFactura.as_view(), name='listarFactura'),
    path('FacturaRetirada/<int:id>/', views.ListarFacturaRetirada.as_view(), name='FacturaRetirada'),
    path('crear_factura/<int:cliente_id>/',crear_factura),
    path('verFactura/<int:p>',views.VerFactura.as_view(), name='verFactura'),
    path('verFacturaRetirada/<int:p>',views.VerFacturaRetirada.as_view(),name='verFacturaRetirada'),
    path('generarFacturaPDF/<int:p>',views.GenerarFacturaPDF.as_view(), name='generarFacturaPDF'),
    path('listarClientesRetirados', views.ListarClientesRetirados.as_view(), name='listarClientesRetirados'),
        
    path('listar_suspendidos/', views.ListarSuspendidos.as_view(), name='listar_suspendidos'),
    path('listar_requipo/', views.ListarREquipos.as_view(), name='listar_requipo'),
    path('listar_reportAp/', views.ListarClientesAp.as_view(), name='listar_reportAp'),
    path('reporte_suspendidos/', views.ReporteSuspendidos.as_view(), name='reporte_suspendidos'),
    path('reporte_requipo/', views.ReporteREquipo.as_view(), name='reporte_requipo'),
    path('reporte_ap/', views.ReporteAp.as_view(), name='reporte_ap'),

    # path('generar_imagen/<int:cliente_id>/',views.GenerarIMG.as_view(), name='generar_imagen'),
    path('todasfacturasPDF/<int:p>',views.TodasFacturasPDF.as_view(), name='todasfacturasPDF'),
    # path('verManualDeUsuario/<str:pagina>/',views.VerManualDeUsuario.as_view(), name='verManualDeUsuario')
]

