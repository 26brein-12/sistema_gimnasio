
from django.shortcuts import render
from .models import Socio

def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'socios/lista.html', {'socios': socios})

from django.shortcuts import render, redirect
from .models import Socio

def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'socios/lista.html', {'socios': socios})


def crear_socio(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')

        Socio.objects.create(
            documento=documento,
            nombres=nombres,
            apellidos=apellidos,
            telefono=telefono,
            correo=correo
        )

        return redirect('socios:lista_socios')

    return render(request, 'socios/crear.html')

def editar_socio(request, id_socio):
    socio = Socio.objects.get(id_socio=id_socio)

    if request.method == 'POST':
        socio.documento = request.POST.get('documento')
        socio.nombres = request.POST.get('nombres')
        socio.apellidos = request.POST.get('apellidos')
        socio.telefono = request.POST.get('telefono')
        socio.correo = request.POST.get('correo')

        socio.save()

        return redirect('socios:lista_socios')

    return render(request, 'socios/editar.html', {'socio': socio})

def eliminar_socio(request, id_socio):
    socio = Socio.objects.get(id_socio=id_socio)

    if request.method == 'POST':
        socio.delete()
        return redirect('socios:lista_socios')

    return render(request, 'socios/eliminar.html', {'socio': socio})


