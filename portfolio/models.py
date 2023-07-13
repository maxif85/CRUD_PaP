from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(null=True, upload_to="projects")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
