from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls')),  # For django-allauth
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
