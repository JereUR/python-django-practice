from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(auto_now_add=True)
