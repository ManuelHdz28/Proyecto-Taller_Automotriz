# ! views.py Aplicaciones/Taller
from django.shortcuts import render
from .models import Repuesto
from django.shortcuts import redirect

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
        
        return redirect('repuestos')
    else:
        return render(request, 'crear_repuesto.html')
    
def eliminar_repuesto(request, id_repuesto):
    """
     * Elimina un repuesto de la base de datos.
    """
    try:
        repuesto = Repuesto.objects.get(id_repuesto=id_repuesto)
        repuesto.delete()
        return redirect('repuestos')
    except Repuesto.DoesNotExist:
        return render(request, 'error.html', {'message': 'Repuesto no encontrado.'})  # * Manejo de error si el repuesto no existe
    
        
        
        