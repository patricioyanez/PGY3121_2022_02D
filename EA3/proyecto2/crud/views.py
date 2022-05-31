from django.shortcuts import render

# Create your views here.

def marcaView(request):
    return render(request, 'marca.html', {'nombre': 'constanza'})

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

       # if 'btnGrabar' in request.POST:
        #    if id < 1: # ORM Object relational Mapping
                


        
        #elif 'btnListar' in request.POST:
        


    return render(request, 'categoria.html', {'nombre': 'constanza'})