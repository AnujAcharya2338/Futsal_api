from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Futsal, Booking
from .serializers import UserSerializer,FutsalSerializer,BookingSerializer
from rest_framework.permissions import IsAuthenticated

class FutsalViewset(viewsets.ModelViewSet):
    queryset = Futsal.objects.all()
    serializer_class = FutsalSerializer
        
class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
            
