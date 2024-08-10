from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Project API",
      default_version='v1',
      description="API documentation for Project App",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourproject.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts', include('applications.posts.urls')),
    path('projects/', include('applications.projects.urls')),
    path('properties/', include('applications.properties.urls')),
    path('budgets/', include('applications.budgets.urls')),
    path('', include('applications.sitecomponents.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^login/$', RedirectView.as_view(url='/accounts/login/', permanent=True)),
    re_path(r'^logout/$', RedirectView.as_view(url='/accounts/logout/', permanent=True)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)