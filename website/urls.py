from django.urls import path
from .views import home, single, my_posts

urlpatterns = [
    path('', home, name='home'),
    path('single/<int:pk>', single, name='single'),
    path('mypost/', my_posts, name='mypost'),
]
