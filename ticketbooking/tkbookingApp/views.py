from django import views
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets, generics, status, permissions, mixins
from .perms import CommentOwnerPerms
from drf_yasg.utils import swagger_auto_schema
from .models import Category, Buses, Customers, Routes, Seats, Ticketbooking, User, Comment
from .serializers import BusSerializer, CategorySerializer, RouteSerializer, SeatSerializer, TicketbookingSerializer, UserSerializer, CommentSerializer, CreateCommentSerializer

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'current_user':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], url_path="current-user", detail=False)
    def current_user(self, request):
        return Response(self.serializer_class(request.user, context={'request': request}).data,
                        status=status.HTTP_200_OK)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset =  Category.objects.filter(active = True)
    serializer_class = CategorySerializer

class BusViewSet(viewsets.ModelViewSet):
    queryset =  Buses.objects.filter(active = True)
    serializer_class = BusSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset =  Seats.objects.filter(active = True)
    serializer_class = SeatSerializer
    
class RouteViewSet(viewsets.ModelViewSet):
    queryset =  Routes.objects.filter(active = True)
    serializer_class = RouteSerializer
    
    @swagger_auto_schema(
        operation_description='Get the comments of a lesson',
        responses={
            status.HTTP_200_OK: CommentSerializer()
        }
    )
    
    @action(methods=['get'], url_path='comments', detail=True)
    def get_comments(self, request, pk):
        routes = self.get_object()
        comments = routes.comments.select_related('user').filter(active=True)

        return Response(CommentSerializer(comments, many=True).data,
                        status=status.HTTP_200_OK)

class CommentViewSet(viewsets.ViewSet, generics.CreateAPIView,
                     generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Comment.objects.filter(active=True)
    serializer_class = CreateCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            return [CommentOwnerPerms()]

        return [permissions.IsAuthenticated()]

class TicketbookingViewSet(viewsets.ModelViewSet):
    queryset =  Ticketbooking.objects.filter(active = True)
    serializer_class = TicketbookingSerializer
    


# Create your views here.
