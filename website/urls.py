from django.urls import path
from .views import home, single

urlpatterns = [
    path('', home, name='home'),
    path('single/<int:pk>', single, name='single'),
]
