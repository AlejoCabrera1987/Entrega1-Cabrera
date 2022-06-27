from django.urls import path, re_path
from coder_course import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
   

    path('index-2', views.index2),
    path('insumos',views.insumos, name="Insumos"),
    path('tareas',views.tareas, name="Tareas"),
    path('rubros',views.rubros, name="Rubros"),
    path('familias/agregar',views.familias, name="Familias"),
    path('iniciar',views.iniciar, name="Iniciar"),
    #path('cargarFamilia',views.cargarfamilias, name="cargarFamilia"),
    path('familias/busquedaCodigo',views.busquedaCodigo, name="BusquedaCodigo"),
    path('buscar/',views.buscar),
    path('leerFamilias',views.leerFamilias, name="leerFamilias"),
    path('familias/list',views.FamiliasList.as_view(), name ="List"),
    re_path(r'^(?P<pk>\d+)$',views.FamiliasDetalle.as_view(), name="Detail"),
    re_path(r'^nuevo$',views.FamiliasCreacion.as_view(), name="New"),
    re_path(r'^editar/(?P<pk>\d+)$',views.FamiliasUpdate.as_view(), name="Edit"),
    re_path(r'^borrar/(?P<pk>\d+)$',views.FamiliasDelete.as_view(), name="Delete"),
    path('login',views.login_request, name='Login'),
    path('logout', LogoutView.as_view (template_name="coder_course/logout.html"), name = 'Logout'),
    path('register',views.register, name='Register'),
    path('editarPerfil',views.editarPerfil, name="Editar Perfil"),
    path('agregarAvatar',views.agregarAvatar, name="Agregar Avatar"),

]