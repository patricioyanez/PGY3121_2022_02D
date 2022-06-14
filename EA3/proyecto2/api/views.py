from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from crud.models import Categoria
from api.serializers import CategoriaSerializer
# Create your views here.

@csrf_exempt
@api_view(['POST', 'GET'])
def apiCategoria(request):

    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def apiCategoriaDetalle(request, buscarId):

    try:
        id = int(buscarId)
        categoria = Categoria.objects.get(pk=id)
    except:
        return Response(status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(categoria, data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        categoria.delete()
        return Response(status = status.HTTP_200_OK)        
