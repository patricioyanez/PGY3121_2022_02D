from django.urls import path
from . import views
urlpatterns = [
        path('marca', views.marcaView, name="marca")
            ]