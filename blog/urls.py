from django.urls import path
from . import views

urlpatterns = [
    path('',views.listar_pub,name='listar_pub'),
    path('pub/<int:pk>',views.detalle_pub,name='detalle_pub'),
    path('pub/nueva', views.nueva_pub, name='nueva_pub'),
    path('pub/<int:pk>/editar/', views.editar_pub, name='editar_pub'),
    path('borradores/', views.lista_borradores, name='lista_borradores'),
    path('pub/<pk>/publicar/', views.publicar_publicacion, name='publicar_publicacion'),
    path('pub/<pk>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),
]
