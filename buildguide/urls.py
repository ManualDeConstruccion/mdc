from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings  # Importa settings
from django.conf.urls.static import static  # Importa static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts', include('applications.posts.urls')),
    path('projects/', include('applications.projects.urls')),
    path('properties/', include('applications.properties.urls')),
    path('budgets/', include('applications.budgets.urls')),
    path('', include('applications.sitecomponents.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^login/$', RedirectView.as_view(url='/accounts/login/', permanent=True)),
    re_path(r'^logout/$', RedirectView.as_view(url='/accounts/logout/', permanent=True))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)