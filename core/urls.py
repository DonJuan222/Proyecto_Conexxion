from django.urls import path
from . import views

urlpatterns = [
    path('', views.Panel.as_view(), name='panel'),
    path('login', views.Login.as_view(), name='login'),
    path('salir', views.Salir.as_view(), name='salir'),
    path('perfil/<str:modo>/<int:p>', views.Perfil.as_view(), name='perfil'),
                                                           
    path('crearUsuario',views.CrearUsuario.as_view(), name='crearUsuario'),
    path('listarUsuarios', views.ListarUsuarios.as_view(), name='listarUsuarios'),
  
]