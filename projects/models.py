from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technology = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    
#Forma en la que Django va convertir los datos a json