from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.filter(is_deleted=False)
    serializer_class = TeacherSerializer

# Create your views here.
