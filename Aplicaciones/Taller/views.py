# ! views.py Aplicaciones/Taller
from django.shortcuts import render
from .models import Repuesto
from .models import Vehiculo  # * Importa el modelo Vehiculo para la gestión de vehículos
from .models import FotoVehiculo  # * Importa el modelo FotoVehiculo para manejar las fotos de los vehículos
from .models import TipoMantenimiento  # * Importa el modelo TipoMantenimiento para manejar los tipos de mantenimiento
from .models import Mantenimiento  # * Importa el modelo Mantenimiento para manejar los mantenimientos
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
        placa = request.POST.get('placa_vehiculo')  #* ← obtener la placa
        nombre = request.POST.get('nombre_propietario')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        anio = request.POST.get('anio')
        fotos = request.FILES.getlist('fotos')

            
        if len(fotos) != 4:
            return render(request, 'gestion_vehiculos.html', {
            'error': 'Debes subir exactamente 4 fotos del vehículo.',
            'gestion_vehiculos': Vehiculo.objects.all()
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

        messages.success(request, 'Vehículo creado exitosamente.')  # * Mensaje de éxito al crear un vehículo
        return redirect('gestion_vehiculos')  # * ajusta esto a tu URL de redirección
    else:
        return render(request, 'gestion_vehiculos.html', {
            'error': os.error,
            'gestion_vehiculos': Vehiculo.objects.all(),
            'abrir_modal': True
        })



def detalle_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    return render(request, 'detalle_vehiculo.html', {'vehiculo': vehiculo})

def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)

    # ~ Eliminar cada imagen físicamente
    for foto in vehiculo.fotos.all():
        if foto.imagen and os.path.isfile(foto.imagen.path):
            os.remove(foto.imagen.path)

    # ~ Eliminar el vehículo (esto elimina los registros de FotoVehiculo por CASCADE)
    vehiculo.delete()
    messages.success(request, 'Vehículo eliminado exitosamente.')  # * Mensaje de éxito al eliminar el vehículo
    return redirect('gestion_vehiculos')  # * Cambia esto al nombre de tu vista destino

def editar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)

    if request.method == 'POST':
        vehiculo.placa_vehiculo = request.POST.get('placa_vehiculo')
        vehiculo.nombre_propietario = request.POST.get('nombre_propietario')
        vehiculo.marca = request.POST.get('marca')
        vehiculo.modelo = request.POST.get('modelo')
        vehiculo.anio = request.POST.get('anio')
        vehiculo.save()
        messages.success(request, 'Vehículo editado exitosamente.')  # * Mensaje de éxito al editar el vehículo
        return redirect('detalle_vehiculo', id=vehiculo.id)

    return render(request, 'editar_vehiculo.html', {'vehiculo': vehiculo})

def tipos_mantenimiento(request):
    
    tipos_mantenimiento = TipoMantenimiento.objects.all()  # * Recibe todos los tipos de mantenimiento de la base de datos
    """
     * Render the type of maintenance page.
    """
    return render(request, 'tipos_mantenimiento.html', {'tipos_mantenimiento': tipos_mantenimiento})  # * Renderiza la plantilla 'tipos_mantenimiento.html'

def crear_tipo_mantenimiento(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_mantenimiento')
        precio = request.POST.get('precio_mantenimiento')

        TipoMantenimiento.objects.create(
            nombre_mantenimiento=nombre,
            precio_mantenimiento=precio
        )
        
        messages.success(request, 'Tipo de mantenimiento creado exitosamente.')  # * Mensaje de éxito al crear un tipo de mantenimiento
        
        return redirect('tipos_mantenimiento')
    else:
        return render(request, 'tipos_mantenimiento.html')

def eliminar_tipo_mantenimiento(request, id_mantenimiento):
    try:
        tipo_mantenimiento = TipoMantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
        tipo_mantenimiento.delete()
        messages.success(request, '¡Tipo de mantenimiento eliminado correctamente!')  # * Mensaje de éxito al eliminar un tipo de mantenimiento
        return redirect('tipos_mantenimiento')
    except TipoMantenimiento.DoesNotExist:
        return render(request, 'error.html', {'message': 'Tipo de mantenimiento no encontrado.'})  # * Manejo de error si el tipo de mantenimiento no existe
    
def editar_tipo_mantenimiento(request, id_mantenimiento):
    
    
    """
     * Edita un tipo de mantenimiento existente.
    """
    try:
        tipo_mantenimiento = TipoMantenimiento.objects.get(id_mantenimiento=id_mantenimiento)

        if request.method == 'POST':
            tipo_mantenimiento.nombre_mantenimiento = request.POST.get('nombre_mantenimiento')
            tipo_mantenimiento.precio_mantenimiento = request.POST.get('precio_mantenimiento')
            tipo_mantenimiento.save()
            messages.success(request, 'Tipo de mantenimiento editado exitosamente.')  # * Mensaje de éxito al editar un tipo de mantenimiento
            return redirect('tipos_mantenimiento')

        return render(request, 'editar_tipo_mantenimiento.html', {'tipo_mantenimiento': tipo_mantenimiento})

    except TipoMantenimiento.DoesNotExist:
        return render(request, 'error.html', {'message': 'Tipo de mantenimiento no encontrado.'})  # * Manejo de error si el tipo de mantenimiento no existe
    
    
def mantenimientos(request):
    mantenimientosdbb = Mantenimiento.objects.all()
    vehiculos = Vehiculo.objects.all()
    tipos_mantenimiento = TipoMantenimiento.objects.all()
    repuestos = Repuesto.objects.all()

    return render(request, 'mantenimientos.html', {
        'mantenimientos': mantenimientosdbb,
        'vehiculos': vehiculos, 
        'tipos_mantenimiento': tipos_mantenimiento,
        'repuestos': repuestos
    })


def crear_repuesto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_repuesto')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        cantidad_disponible = request.POST.get('cantidad_disponible')


        # * Crea un nuevo repuesto en la base de datos
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
    
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vehiculo, TipoMantenimiento, Repuesto, Mantenimiento

def crear_mantenimiento(request):
    if request.method == 'POST':
        vehiculo_id = request.POST.get('vehiculo')
        tipo_mantenimiento_id = request.POST.get('tipo_mantenimiento')
        repuestos_ids = request.POST.getlist('repuestos')
        fecha_mantenimiento = request.POST.get('fecha_mantenimiento')
        precio_total = request.POST.get('precioTotal')

        # Obtener objetos relacionados usando claves correctas
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        tipo_mantenimiento = get_object_or_404(TipoMantenimiento, id_mantenimiento=tipo_mantenimiento_id)
        repuestos = Repuesto.objects.filter(id_repuesto__in=repuestos_ids)

        # Crear el mantenimiento (sin asignar repuestos aún)
        mantenimiento = Mantenimiento.objects.create(
            vehiculo=vehiculo,
            tipo_mantenimiento=tipo_mantenimiento,
            fecha_mantenimiento=fecha_mantenimiento,
            precioTotal=precio_total
        )

        # Asignar repuestos después de guardar
        mantenimiento.Repuestos.set(repuestos)

        messages.success(request, '¡Mantenimiento creado exitosamente!')
        return redirect('mantenimientos')
    
    return render(request, 'mantenimiento.html')

def eliminar_mantenimiento(request, id_mantenimiento):
    """
     * Elimina un mantenimiento por su ID.
    """
    try:
        mantenimiento = Mantenimiento.objects.get(id_mantenimientov=id_mantenimiento)
        mantenimiento.delete()
        messages.success(request, '¡Mantenimiento eliminado correctamente!')  # * Mensaje de éxito al eliminar un mantenimiento
        return redirect('mantenimientos')
    except Mantenimiento.DoesNotExist:
        return render(request, 'error.html', {'message': 'Mantenimiento no encontrado.'})  # * Manejo de error si el mantenimiento no existe
    
def editar_mantenimiento(request, id_mantenimiento):
    """
     * Edita un mantenimiento existente.
    """
    try:
        mantenimiento = Mantenimiento.objects.get(id_mantenimientov=id_mantenimiento)

        if request.method == 'POST':
            mantenimiento.vehiculo = request.POST.get('vehiculo')
            mantenimiento.tipo_mantenimiento = request.POST.get('tipo_mantenimiento')
            mantenimiento.fecha_mantenimiento = request.POST.get('fecha_mantenimiento')
            mantenimiento.save()
            messages.success(request, 'Mantenimiento editado exitosamente.')  # * Mensaje de éxito al editar un mantenimiento
            return redirect('mantenimientos')

        return render(request, 'editar_mantenimiento.html', {'mantenimiento': mantenimiento})

    except Mantenimiento.DoesNotExist:
        return render(request, 'error.html', {'message': 'Mantenimiento no encontrado.'})  # * Manejo de error si el mantenimiento no existe

    
