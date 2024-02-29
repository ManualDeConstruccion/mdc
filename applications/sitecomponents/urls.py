from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  # Asigna la vista home a la URL raíz
]
