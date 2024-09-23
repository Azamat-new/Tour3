from rest_framework import serializers
from .models import MyUser
from tour.models import Tour, Booking


class MyUserSerializer(serializers.ModelSerializer):
    favorite_tours = serializers.StringRelatedField(many=True)
    bookings = serializers.StringRelatedField()

    class Meta:
        model = MyUser
        fields = ['username', 'phone_number', 'email', 'favorite_tours', 'bookings']


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password']


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'first_name', 'last_name']


