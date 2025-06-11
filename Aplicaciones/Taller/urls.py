# * urls.py Aplicaciones/Taller
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # * Maps the root URL to the index view
    path('repuestos/', views.repuestos, name="repuestos"),  # * Mapas de la URL 'repuestos/' a la vista repuestos
    path('crear_repuesto/', views.crear_repuesto, name="crear_repuesto"),
    path('eliminar_repuesto/<id_repuesto>/', views.eliminar_repuesto, name="eliminar_repuesto"),  # * mapea la URL 'eliminar_repuesto/<id_repuesto>/' a la vista eliminar_repuesto
    path('editar_repuesto/<int:id_repuesto>/', views.editar_repuesto, name="editar_repuesto"),  # * mapea la URL 'editar_repuesto/<id_repuesto>/' a la vista editar_repuesto
]

