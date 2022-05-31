from django.urls import path
from . import views
urlpatterns = [
        path('marca', views.marcaView, name="marca"),
        path('categoria', views.categoriaView, name="categoria"),
        path('categoria/<int:id>/', views.categoriaLeerView, name="categoria"),
            ]