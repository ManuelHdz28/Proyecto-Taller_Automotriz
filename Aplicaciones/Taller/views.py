# ! views.py Aplicaciones/Taller
from django.shortcuts import render
from .models import Repuesto
from .models import Vehiculo  # * Importa el modelo Vehiculo para la gestión de vehículos
from .models import FotoVehiculo  # * Importa el modelo FotoVehiculo para manejar las fotos de los vehículos
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
import os  # * Importa el módulo os para manejar archivos del sistema operativo


# Create your views here.
def index(request):
    """
     * Render the index page of the Taller application.
    """
    return render(request, 'index.html')

def repuestos(request):
    
    repuestosdbb = Repuesto.objects.all()  # * Recibe todos los repuestos de la base de datos
    
    """
     * Render the list of repuestos.
    """
    return render(request, 'repuestos.html', {'repuestos': repuestosdbb})  # * Pasa los repuestos a la plantilla 'repuestos.html' 

def gestion_vehiculos(request):

    gestionvehiculos = Vehiculo.objects.all()   # * Recibe todos los vehículos de la base de datos para la gestión de vehículos

    """
     * Render the vehicle management page.
    """
    return render(request, 'gestion_vehiculos.html', {'gestion_vehiculos': gestionvehiculos})  # * Renderiza la plantilla 'gestion_vehiculos.html'

def crear_repuesto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_repuesto')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        cantidad_disponible = request.POST.get('cantidad_disponible')


        Repuesto.objects.create(
            nombre_repuesto=nombre,
            descripcion=descripcion,
            precio=precio,
            cantidad_disponible=cantidad_disponible
        )
        
        messages.success(request, 'Repuesto creado exitosamente.')  # * Mensaje de éxito al crear un repuesto
        
        return redirect('repuestos')
    else:
        return render(request, 'repuestos.html')

def eliminar_repuesto(request, id_repuesto): # * Vista para eliminar una carrera por su ID
    # * Se busca la carrera por su ID y se elimina
    try:
        repuestodb = Repuesto.objects.get(id_repuesto=id_repuesto)
        repuestodb.delete()
        messages.success(request, '¡Repuesto Borrado de la base de datos correctamente!') # * Mensaje de éxito al eliminar el repuesto
        return redirect('/repuestos')
    except Repuesto.DoesNotExist:
        return render(request, 'error.html', {'message': 'Repuesto no encontrado.'})  # * Manejo de error si el repuesto no existe
        
def editar_repuesto(request, id_repuesto):
    """
     * Edita un repuesto existente.
    """
    try:
        repuesto = Repuesto.objects.get(id_repuesto=id_repuesto)
        
        if request.method == 'POST':
            repuesto.nombre_repuesto = request.POST.get('nombre_repuesto')
            repuesto.descripcion = request.POST.get('descripcion')
            repuesto.precio = request.POST.get('precio')
            repuesto.cantidad_disponible = request.POST.get('cantidad_disponible')
            repuesto.save()
            messages.success(request, 'Repuesto editado exitosamente.') # * Mensaje de éxito al editar un repuesto
            return redirect('repuestos')
        
        return render(request, 'editar_repuestos.html', {'repuesto': repuesto})
    
    except Repuesto.DoesNotExist:
        return render(request, 'error.html', {'message': 'Repuesto no encontrado.'})  # * Manejo de error si el repuesto no existe
    
def crear_vehiculo(request):
    if request.method == 'POST':
        placa = request.POST.get('placa_vehiculo')  # ← obtener la placa
        nombre = request.POST.get('nombre_propietario')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        anio = request.POST.get('anio')
        fotos = request.FILES.getlist('fotos')

        if len(fotos) != 4:
            return render(request, 'vehiculos/crear_vehiculo.html', {
                'error': 'Debes subir exactamente 4 fotos del vehículo.',
            })

        vehiculo = Vehiculo.objects.create(
            placa_vehiculo=placa,
            nombre_propietario=nombre,
            marca=marca,
            modelo=modelo,
            anio=anio
        )

        for imagen in fotos:
            FotoVehiculo.objects.create(vehiculo=vehiculo, imagen=imagen)

        return redirect('gestion_vehiculos')  # ajusta esto a tu URL de redirección
    else:
        return render(request, 'gestion_vehiculos.html')



def detalle_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    return render(request, 'detalle_vehiculo.html', {'vehiculo': vehiculo})

def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)

    # Eliminar cada imagen físicamente
    for foto in vehiculo.fotos.all():
        if foto.imagen and os.path.isfile(foto.imagen.path):
            os.remove(foto.imagen.path)

    # Eliminar el vehículo (esto elimina los registros de FotoVehiculo por CASCADE)
    vehiculo.delete()
    messages.success(request, 'Vehículo eliminado exitosamente.')  # Mensaje de éxito al eliminar el vehículo
    return redirect('gestion_vehiculos')  # Cambia esto al nombre de tu vista destino
