from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):#Indicamos que consultas se van a poder realizar
    queryset = Project.objects.all() #Consulatr todos los datos de una tabla
    permission_classes = [permissions.AllowAny] #Cualquier cliente puede solicitar datos a la aplicacion (Se puede complementar con si esta autenticado)
    serializer_class = ProjectSerializer
    
    
