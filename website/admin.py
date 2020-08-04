from django.contrib import admin
from .models import Post


class PostModels(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'user', 'id', 'date_post']


admin.site.register(Post, PostModels)
