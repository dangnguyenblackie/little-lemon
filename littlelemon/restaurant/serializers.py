from rest_framework import serializers
from .models import Booking, MenuItem
from django.contrib.auth.models import User

# User
class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# Booking Table
class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

# MenuItem Table
class MenuItemSerializer (serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'