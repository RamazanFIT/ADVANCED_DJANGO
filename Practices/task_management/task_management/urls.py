"""
URL configuration for task_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from email_app.views import CVViewSet
from jobs.views import JobPostViewSet, JobApplicationViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="CV API",
      default_version='v1',
      description="API для управления резюме",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourcompany.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = DefaultRouter()
router.register(r'cvs', CVViewSet, basename='cv')
router.register(r'jobs', JobPostViewSet, basename='job')
router.register(r'applications', JobApplicationViewSet, basename='application')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path("api/", include("core.urls")),
    path("practise3/", include("practise3.urls")),
    path('', include('todolist.urls')),
    path('', include('additional_tasks.urls')),
    path('', include('email_app.urls')),
    path('api/', include('api.urls')),
    path('api/expenses/', include('expenses.urls')),
]
