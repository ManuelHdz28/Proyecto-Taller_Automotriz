from django.db import models # * Importa el módulo models de Django para definir modelos de base de datos


# & Aplicaciones/Taller/models.py

# ^ Modelo de Repuesto
# * Este modelo representa un repuesto que puede ser utilizado en un vehículo.
class Repuesto(models.Model): # * Modelo para representar un repuesto
    # * Atributos del modelo
    id_repuesto = models.AutoField(primary_key=True) # ~ Campo de clave primaria autoincremental
    nombre_repuesto = models.CharField(max_length=100) 
    descripcion = models.TextField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField() # ~ tipo de dato para cantidades enteras positivas

    def __str__(self): # * Método para representar el objeto como una cadena
        return self.nombre_repuesto # ~ Devuelve el nombre del repuesto como representación en cadena
    
# ^ Modelo de Vehiculo
# * Este modelo representa un vehículo que puede tener mantenimientos y fotos asociadas.    
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

# ^ Modelo de FotoVehiculo
# * Este modelo representa una foto asociada a un vehículo.    
class FotoVehiculo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='fotos') # * Relación con el modelo Vehiculo, eliminando fotos si se elimina el vehículo
    imagen = models.ImageField(upload_to='fotos_vehiculos/')  # ~ Requiere Pillow instalado

    def __str__(self):
        return f"Foto de {self.vehiculo}"

# ^ Modelo de TipoMantenimiento
# * Este modelo representa un tipo de mantenimiento que puede ser realizado en un vehículo. 
class TipoMantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)  # ~ Campo de clave primaria autoincremental
    nombre_mantenimiento = models.CharField(max_length=100, unique=True)  # * Nombre del tipo de mantenimiento sea único
    precio_mantenimiento = models.DecimalField(max_digits=10, decimal_places=2)  # * Precio del mantenimiento

    def __str__(self):
        return self.nombre_mantenimiento  # ~ Devuelve el nombre del tipo de mantenimiento como representación en cadena

# ^ Modelo de Mantenimiento
# * Este modelo representa un mantenimiento realizado en un vehículo, que puede incluir múltiples repuestos.   
class Mantenimiento(models.Model):
    id_mantenimientov = models.AutoField(primary_key=True)  # ~ Campo de clave primaria autoincremental
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='mantenimientos')  # * Relación con el modelo Vehiculo
    tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE, related_name='mantenimientos')  # * Relación con el modelo TipoMantenimiento
    Repuestos = models.ManyToManyField(Repuesto, blank=True, related_name='mantenimientos')  # * Relación con el modelo Repuesto, permitiendo múltiples repuestos por mantenimiento
    fecha_mantenimiento = models.DateField()  # * Fecha del mantenimiento
    precioTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # * Precio total del mantenimiento

    def __str__(self):
        return f"Mantenimiento de {self.vehiculo} - {self.tipo_mantenimiento}"  # ~ Devuelve una representación del mantenimiento como cadena

    
