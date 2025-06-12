# * urls.py Aplicaciones/Taller
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # * Maps the root URL to the index view
    #^ seccion de repuestos
    path('repuestos/', views.repuestos, name="repuestos"),  # * Mapas de la URL 'repuestos/' a la vista repuestos
    path('crear_repuesto/', views.crear_repuesto, name="crear_repuesto"),
    path('eliminar_repuesto/<id_repuesto>/', views.eliminar_repuesto, name="eliminar_repuesto"),  # * mapea la URL 'eliminar_repuesto/<id_repuesto>/' a la vista eliminar_repuesto
    path('editar_repuesto/<int:id_repuesto>/', views.editar_repuesto, name="editar_repuesto"),  # * mapea la URL 'editar_repuesto/<id_repuesto>/' a la vista editar_repuesto
    
    #^ seccion de vehiculos
    path('gestion_vehiculos/', views.gestion_vehiculos, name="gestion_vehiculos"),  # * Mapea la URL 'gestion_vehiculos/' a la vista gestion_vehiculos
    path('crear_vehiculo/', views.crear_vehiculo, name="crear_vehiculo"),  # * Mapea la URL 'crear_vehiculo/' a la vista crear_vehiculo
    path('vehiculo/<int:id>/', views.detalle_vehiculo, name='detalle_vehiculo'), # * Mapea la URL 'vehiculo/<id>/' a la vista detalle_vehiculo
    path('eliminar_vehiculo/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),  # * Mapea la URL 'eliminar_vehiculo/<id>/' a la vista eliminar_vehiculo
    path('editar_vehiculo/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'),  # * Mapea la URL 'editar_vehiculo/<id>/' a la vista editar_vehiculo
    
    #^ seccion de tipos de mantenimiento
    path('tipos_mantenimiento/', views.tipos_mantenimiento, name="tipos_mantenimiento"),  # * Mapea la URL 'tipos_mantenimiento/' a la vista tipos_mantenimiento
    path('crear_tipo_mantenimiento/', views.crear_tipo_mantenimiento, name="crear_tipo_mantenimiento"),  # * Mapea la URL 'crear_tipo_mantenimiento/' a la vista crear_tipo_mantenimiento
    path('eliminar_tipo_mantenimiento/<int:id_mantenimiento>/', views.eliminar_tipo_mantenimiento, name="eliminar_tipo_mantenimiento"),  # * Mapea la URL 'eliminar_tipo_mantenimiento/<id_tipo_mantenimiento>/' a la vista eliminar_tipo_mantenimiento
    
]

