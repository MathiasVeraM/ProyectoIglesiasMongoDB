from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_sacramentos),
    path('crear/', views.crear_sacramento),
    path('editar/<str:id>/', views.editar_sacramento),
    path('eliminar/<str:id>/', views.eliminar_sacramento),
]