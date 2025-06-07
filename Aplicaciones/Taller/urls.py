# * urls.py Aplicaciones/Taller
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # * Maps the root URL to the index view
    path('repuestos/', views.repuestos, name="repuestos"),  # * Mapas de la URL 'repuestos/' a la vista repuestos
]

