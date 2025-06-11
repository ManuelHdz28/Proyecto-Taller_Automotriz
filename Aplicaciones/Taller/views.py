# ! views.py Aplicaciones/Taller
from django.shortcuts import render
from .models import Repuesto
from django.shortcuts import redirect
from django.contrib import messages

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
    
def eliminar_repuesto(request, id_repuesto):
    """
     * Elimina un repuesto de la base de datos.
    """
    try:
        repuesto = Repuesto.objects.get(id_repuesto=id_repuesto)
        repuesto.delete()
        messages.success(request, 'Repuesto eliminado exitosamente.')  # * Mensaje de éxito al eliminar un repuesto
        return redirect('repuestos')
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
        