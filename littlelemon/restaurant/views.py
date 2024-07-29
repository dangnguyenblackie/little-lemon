from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemsView (generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView (generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet (viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer