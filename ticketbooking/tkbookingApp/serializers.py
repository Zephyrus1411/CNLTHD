from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Category, Buses, Customers, Routes, Seats, Ticketbooking, User, Comment

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(source='avatar')

    def get_avatar(self, obj):
        request = self.context['request']
        if obj.avatar and not obj.avatar.name.startswith("/static"):

            path = '/static/%s' % obj.avatar.name

            return request.build_absolute_uri(path)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'username', 'password', 'email',
                  'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()

        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['type']

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buses
        fields = ['bus_name']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = ['seat_numb']

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = ['begining', 'destination', 'cost']

class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'user', 'routes']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        exclude = ['active']

class TicketbookingSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    buses = BusSerializer()
    seats = SeatSerializer()
    routes = RouteSerializer()
    class Meta:
        model = Ticketbooking
        fields = ['id', 'cus_name', 'numb_phone', 'created_date', 'image', 'buses',  'category', 'seats', 'routes']
        
