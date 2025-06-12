from django.contrib import admin
from .models import Repuesto, Vehiculo, FotoVehiculo

# Register your models here.
admin.site.register(Repuesto)
admin.site.register(Vehiculo)
admin.site.register(FotoVehiculo)  # Register the FotoVehiculo model in the admin interface
