from django.shortcuts import render

# Create your views here.

def marcaView(request):
    return render(request, 'marca.html', {'nombre': 'constanza'})

