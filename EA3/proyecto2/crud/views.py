from django.shortcuts import render

from crud.models import Categoria

# Create your views here.

def marcaView(request):
    return render(request, 'marca.html', {'nombre': 'constanza'})

def categoriaLeerView(request, id):
    contexto = {}
    if not id is None:
        fila = Categoria.objects.get(pk = id)
        contexto = {'fila': fila}

    return render(request, 'categoria.html', contexto)

def categoriaView(request):
    contexto = {}
    if request.method == 'POST':
        # capturar datos del form
        id = int("0" + request.POST["txtId"])
        nombre = request.POST["txtNombre"]
        activo = False
        if 'chkActivo' in request.POST:
            activo = True

        # detectar que botón fue presionado

        if 'btnGrabar' in request.POST:
            if id < 1: # ORM Object relational Mapping
                Categoria.objects.create(nombre = nombre, activo = activo) 
            else:
                item = Categoria.objects.get(pk = id)
                item.nombre = nombre
                item.activo = activo
                item.save()     
            contexto = {'mensaje': 'Los datos fueron guardados'}

        
        elif 'btnListar' in request.POST:
            listado = Categoria.objects.all()
            contexto = {'listado': listado }


    return render(request, 'categoria.html', contexto)