from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    title = models.CharField(max_length=200)  # Se usa en posts_list.html
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
