from django.db import models

# Create your models here.
class Repuesto(models.Model): # * Modelo para representar un repuesto
    # * Atributos del modelo
    id_repuesto = models.AutoField(primary_key=True) # ~ Campo de clave primaria autoincremental
    nombre_repuesto = models.CharField(max_length=100) 
    descripcion = models.TextField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField() # ~ tipo de dato para cantidades enteras positivas

    def __str__(self): # * Método para representar el objeto como una cadena
        return self.nombre # ~ Devuelve el nombre del repuesto como representación en cadena