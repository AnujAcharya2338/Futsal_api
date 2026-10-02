from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Futsal, Booking
from .serializers import UserSerializer,FutsalSerializer,BookingSerializer

class FutsalViewset(viewsets.ModelViewSet):
        queryset = Futsal.objects.all()
        serializer_class = FutsalSerializer
        

# Create your views here.
