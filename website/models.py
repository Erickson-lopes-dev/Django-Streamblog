from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=60)
    sub_title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # photo = models.ImageField(upload_to='photo_user/', null=True, blank=True)
    date_post = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


