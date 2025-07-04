from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_personas),
    path('crear/', views.crear_persona),
    path('editar/<str:id>/', views.editar_persona),
    path('eliminar/<str:id>/', views.eliminar_persona),
    path('detalle/<str:id>/', views.detalle_persona)
]