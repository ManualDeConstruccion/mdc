"""
URL configuration for buildguide project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings  # Importa settings
from django.conf.urls.static import static  # Importa static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts', include('applications.posts.urls')),
    #path('projects/', include('applications.projects.urls')),
    #path('properties/', include('applications.properties.urls')),
    path('budgets/', include('applications.budgets.urls')),
    path('', include('applications.sitecomponents.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^login/$', RedirectView.as_view(url='/accounts/login/', permanent=True)),
    re_path(r'^logout/$', RedirectView.as_view(url='/accounts/logout/', permanent=True))
]