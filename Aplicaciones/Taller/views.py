from django.shortcuts import render # * Importa render para renderizar plantillas HTML
from .models import Repuesto # * Importa el modelo Repuesto para la gestión de repuestos
from .models import Vehiculo  # * Importa el modelo Vehiculo para la gestión de vehículos
from .models import FotoVehiculo  # * Importa el modelo FotoVehiculo para manejar las fotos de los vehículos
from .models import TipoMantenimiento  # * Importa el modelo TipoMantenimiento para manejar los tipos de mantenimiento
from .models import Mantenimiento  # * Importa el modelo Mantenimiento para manejar los mantenimientos
from django.shortcuts import redirect # * Importa redirect para redirigir a otras vistas
from django.contrib import messages # * Importa messages para mostrar mensajes de éxito o error al usuario
from django.shortcuts import render, get_object_or_404 # * Importa render y get_object_or_404 para manejar vistas y obtener objetos de la base de datos
from django.http import JsonResponse  # * Importa JsonResponse para manejar respuestas JSON
import os  # * Importa el módulo os para manejar archivos del sistema operativo

# & views.py Aplicaciones/Taller

# Create your views here.

# ^ Vista de índice
def index(request):
    """
     * Render the index page of the Taller application.
    """
    return render(request, 'index.html')

# ^ Vista de repuestos
# ~ Esta vista maneja la visualización y gestión de repuestos en el taller.
def repuestos(request):
    
    repuestosdbb = Repuesto.objects.all()  # * Recibe todos los repuestos de la base de datos
    
    """
     * Render the list of repuestos.
    """
    return render(request, 'repuestos.html', {'repuestos': repuestosdbb})  # * Pasa los repuestos a la plantilla 'repuestos.html' 

# ^ Vista de gestión de vehículos
# ~ Esta vista maneja la visualización y gestión de vehículos en el taller.
def gestion_vehiculos(request):

    gestionvehiculos = Vehiculo.objects.all()   # * Recibe todos los vehículos de la base de datos para la gestión de vehículos

    """
     * Render the vehicle management page.
    """
    return render(request, 'gestion_vehiculos.html', {'gestion_vehiculos': gestionvehiculos})  # * Renderiza la plantilla 'gestion_vehiculos.html'

# ^ Vista para crear un nuevo repuesto
# ~ Esta vista maneja la creación de un nuevo repuesto en el taller.
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

# ^ Vista para eliminar un repuesto por su ID
# ~ Esta vista maneja la eliminación de un repuesto específico de la base de datos.
def eliminar_repuesto(request, id_repuesto): # * Vista para eliminar una carrera por su ID
    # * Se busca la carrera por su ID y se elimina
    try:
        repuestodb = Repuesto.objects.get(id_repuesto=id_repuesto)
        repuestodb.delete()
        messages.success(request, '¡Repuesto Borrado de la base de datos correctamente!') # * Mensaje de éxito al eliminar el repuesto
        return redirect('/repuestos')
    except Repuesto.DoesNotExist:
        return render(request, 'error.html', {'message': 'Repuesto no encontrado.'})  # * Manejo de error si el repuesto no existe

# ^ Vista para editar un repuesto por su ID
# ~ Esta vista maneja la edición de un repuesto específico en la base de datos.     
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

# ^ Vista para crear un nuevo vehículo
# ~ Esta vista maneja la creación de un nuevo vehículo en el taller. 
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


# ^ Vista para mostrar los detalles de un vehículo por su ID
# ~ Esta vista maneja la visualización de los detalles de un vehículo específico, incluyendo sus fotos.
def detalle_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    return render(request, 'detalle_vehiculo.html', {'vehiculo': vehiculo})

# ^ Vista para eliminar un vehículo por su ID
# ~ Esta vista maneja la eliminación de un vehículo específico de la base de datos, incluyendo
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

# ^ Vista para editar un vehículo por su ID
# ~ Esta vista maneja la edición de un vehículo específico en la base de datos.
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

# ^ Vista para manejar los tipos de mantenimiento
# ~ Esta vista maneja la visualización, creación, edición y eliminación de tipos de mantenimiento
def tipos_mantenimiento(request):
    
    tipos_mantenimiento = TipoMantenimiento.objects.all()  # * Recibe todos los tipos de mantenimiento de la base de datos
    """
     * Render the type of maintenance page.
    """
    return render(request, 'tipos_mantenimiento.html', {'tipos_mantenimiento': tipos_mantenimiento})  # * Renderiza la plantilla 'tipos_mantenimiento.html'

# ^ Vista para crear un nuevo tipo de mantenimiento
# ~ Esta vista maneja la creación de un nuevo tipo de mantenimiento en el taller.
def crear_tipo_mantenimiento(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_mantenimiento')
        precio = request.POST.get('precio_mantenimiento')

        # Validación para evitar nombres duplicados
        if TipoMantenimiento.objects.filter(nombre_mantenimiento=nombre).exists(): # * Verifica si ya existe un tipo de mantenimiento con el mismo nombre
            # * Si ya existe, muestra un mensaje de error y redirige a la página
            messages.error(request, 'Ya existe un tipo de mantenimiento con ese nombre.')
            return redirect('tipos_mantenimiento')
        
        TipoMantenimiento.objects.create(
            nombre_mantenimiento=nombre,
            precio_mantenimiento=precio
        )
        
        # * Mensaje de éxito al crear un tipo de mantenimiento
        messages.success(request, 'Tipo de mantenimiento creado exitosamente.') # * Mensaje de éxito al crear un tipo de mantenimiento
        return redirect('tipos_mantenimiento')
    
    return render(request, 'tipos_mantenimiento.html')

# ^ Vista para eliminar un tipo de mantenimiento por su ID
# ~ Esta vista maneja la eliminación de un tipo de mantenimiento específico de la base de datos
def eliminar_tipo_mantenimiento(request, id_mantenimiento):
    try:
        tipo_mantenimiento = TipoMantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
        tipo_mantenimiento.delete()
        messages.success(request, '¡Tipo de mantenimiento eliminado correctamente!')  # * Mensaje de éxito al eliminar un tipo de mantenimiento
        return redirect('tipos_mantenimiento')
    except TipoMantenimiento.DoesNotExist:
        return render(request, 'error.html', {'message': 'Tipo de mantenimiento no encontrado.'})  # * Manejo de error si el tipo de mantenimiento no existe

# ^ Vista para editar un tipo de mantenimiento por su ID
# ~ Esta vista maneja la edición de un tipo de mantenimiento específico en la base de datos  
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
    
# ^ Vista para manejar los mantenimientos
# ~ Esta vista maneja la visualización, creación, edición y eliminación de mantenimientos en el taller.
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

# ^ Vista para crear un nuevo repuesto
# ~ Esta vista maneja la creación de un nuevo repuesto en el taller.
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

# ^ Vista para crear un nuevo mantenimiento
# ~ Esta vista maneja la creación de un nuevo mantenimiento en el taller, incluyendo la asignación de repuestos.
def crear_mantenimiento(request):
    if request.method == 'POST': # * Verifica si la solicitud es POST
        vehiculo_id = request.POST.get('vehiculo')
        tipo_mantenimiento_id = request.POST.get('tipo_mantenimiento')
        repuestos_ids = request.POST.getlist('repuestos')
        fecha_mantenimiento = request.POST.get('fecha_mantenimiento')
        precio_total = request.POST.get('precioTotal')

        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        tipo_mantenimiento = get_object_or_404(TipoMantenimiento, id_mantenimiento=tipo_mantenimiento_id)
        repuestos = Repuesto.objects.filter(id_repuesto__in=repuestos_ids)

        mantenimiento = Mantenimiento.objects.create(
            vehiculo=vehiculo,
            tipo_mantenimiento=tipo_mantenimiento,
            fecha_mantenimiento=fecha_mantenimiento,
            precioTotal=precio_total
        )

        mantenimiento.Repuestos.set(repuestos)

        # ↓↓↓ Reducir cantidad disponible de cada repuesto en 1 unidad
        for repuesto in repuestos:
            if repuesto.cantidad_disponible > 0:
                repuesto.cantidad_disponible -= 1
                repuesto.save()

        messages.success(request, '¡Mantenimiento creado exitosamente!')
        return redirect('mantenimientos')

    return render(request, 'mantenimiento.html')


# ^ Vista para eliminar un mantenimiento por su ID
# ~ Esta vista maneja la eliminación de un mantenimiento específico de la base de datos.
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

# ^ Vista para editar un mantenimiento por su ID
# ~ Esta vista maneja la edición de un mantenimiento específico en la base de datos, permitiendo actualizar los detalles del mantenimiento y los repuestos asociados.   
def editar_mantenimiento(request, id_mantenimiento):
    """
     * Edita un mantenimiento existente.
    """
    mantenimiento = get_object_or_404(Mantenimiento, id_mantenimientov=id_mantenimiento)

    if request.method == 'POST':
        vehiculo_id = request.POST.get('vehiculo')
        tipo_id = request.POST.get('tipo_mantenimiento')
        fecha = request.POST.get('fecha_mantenimiento')
        precio_total = request.POST.get('precioTotal')
        repuestos_ids = request.POST.getlist('repuestos')

        # * Actualizar relaciones ForeignKey
        mantenimiento.vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        mantenimiento.tipo_mantenimiento = get_object_or_404(TipoMantenimiento, id_mantenimiento=tipo_id)
        mantenimiento.fecha_mantenimiento = fecha
        mantenimiento.precioTotal = precio_total
        mantenimiento.save()

        # * Actualizar relación ManyToMany
        mantenimiento.Repuestos.set(Repuesto.objects.filter(id_repuesto__in=repuestos_ids))

        messages.success(request, 'Mantenimiento editado exitosamente.')
        return redirect('mantenimientos')

    # * Repuestos seleccionados para el template
    repuestos_seleccionados = mantenimiento.Repuestos.values_list('id_repuesto', flat=True)

    return render(request, 'editar_mantenimiento.html', {
        'mantenimiento': mantenimiento,
        'vehiculos': Vehiculo.objects.all(),
        'tipos_mantenimiento': TipoMantenimiento.objects.all(),
        'repuestos': Repuesto.objects.all(),
        'repuestos_seleccionados': repuestos_seleccionados,
    })
# ^ Vista para validar el nombre de un tipo de mantenimiento
# ~ Esta vista maneja la validación del nombre de un tipo de mantenimiento para evitar duplicados.
def validar_nombre_tipo_mantenimiento(request):
    nombre = request.GET.get('nombre_mantenimiento', None)
    print("🔍 Nombre recibido para validar:", nombre)
    existe = TipoMantenimiento.objects.filter(nombre_mantenimiento__iexact=nombre).exists()
    print("📦 ¿Existe en la base?:", existe)
    return JsonResponse({'valid': not existe})
