from django.db import models

class noticia(models.Model):
    titulo = models.CharField(max_length=350, blank=False)
    corpo = models.TextField( max_length=10000,blank=False)
    image = models.ImageField(upload_to="static/img/")
    date = models.DateTimeField(blank=False, auto_now=True)
