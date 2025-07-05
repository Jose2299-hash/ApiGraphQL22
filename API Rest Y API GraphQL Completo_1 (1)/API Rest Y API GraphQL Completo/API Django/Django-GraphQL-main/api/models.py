from django.db import models

class Category(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='publicaciones')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
