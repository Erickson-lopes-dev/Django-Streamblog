from django.urls import path
from .views import home, single, my_posts, create, edit

urlpatterns = [
    path('', home, name='home'),
    path('single/<int:pk>', single, name='single'),
    path('mypost/', my_posts, name='mypost'),
    path('create/', create, name='create_post'),
    path('edit/<int:pk>', edit, name='edit_post'),
]
