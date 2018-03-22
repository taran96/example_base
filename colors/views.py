from django.shortcuts import render
from .models import Color
from .serializers import ColorSerializer
from rest_framework import viewsets

# Create your views here.
class ColorView(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer