from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'sitecomponents'

urlpatterns = [
    path('', views.landing, name='landing'),  # Asigna la vista home a la URL raíz
    path('intro/', TemplateView.as_view(template_name='views/intro.html'), name='intro'),
]
