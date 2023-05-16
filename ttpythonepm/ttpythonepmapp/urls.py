from django.urls import path

from .views import *

urlpatterns = [

    path('Info_Grafica', InfoGraficas.as_view() ),
]