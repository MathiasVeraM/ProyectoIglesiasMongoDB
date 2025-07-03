from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_parroquias),
    path('crear/', views.crear_parroquia),
    path('editar/<str:id>/', views.editar_parroquia),
    path('eliminar/<str:id>/', views.eliminar_parroquia),
]