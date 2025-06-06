# ! views.py Aplicaciones/Taller
from django.shortcuts import render

# Create your views here.
def index(request):
    """
     * Render the index page of the Taller application.
    """
    return render(request, 'index.html')