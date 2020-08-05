from django.contrib import admin
from django.urls import path, include
from website.views import django_logout, register, django_login

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/', include('django.contrib.auth.urls')),
    path('login/', django_login),
    path('logout/', django_logout),
    path('register/', register),
    path('', include('website.urls'))
]
