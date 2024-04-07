from django.shortcuts import render, redirect
from .models import Publicacion
from .forms import PublicacionForm

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'lista_publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = Publicacion.objects.get(pk=pk)
    return render(request, 'detalle_publicacion.html', {'publicacion': publicacion})

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm()
    return render(request, 'crear_publicacion.html', {'form': form})

# Otras vistas como editar_publicacion y eliminar_publicacion pueden ser definidas aquí
