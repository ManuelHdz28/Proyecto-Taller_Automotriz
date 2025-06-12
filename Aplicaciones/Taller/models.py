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
        return self.nombre_repuesto # ~ Devuelve el nombre del repuesto como representación en cadena
    
    
class Vehiculo(models.Model): # * Modelo para representar un vehículo
    # * Atributos del modelo
    id = models.AutoField(primary_key=True)  # ~ Campo autoincremental
    placa_vehiculo = models.CharField(max_length=9, unique=True, blank=True)  #~ Visible al usuario
    nombre_propietario = models.CharField(max_length=100)
    marca = models.CharField(max_length=50) 
    modelo = models.CharField(max_length=50) 
    anio = models.PositiveIntegerField() # ~ tipo de dato para años (enteros positivos)
    
    

    def __str__(self): # * Método para representar el objeto como una cadena
        return f"{self.marca} {self.modelo} ({self.anio})" # ~ Devuelve una representación del vehículo como cadena
    
class FotoVehiculo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='fotos') # * Relación con el modelo Vehiculo, eliminando fotos si se elimina el vehículo
    imagen = models.ImageField(upload_to='fotos_vehiculos/')  # Requiere Pillow instalado

    def __str__(self):
        return f"Foto de {self.vehiculo}"
    
 