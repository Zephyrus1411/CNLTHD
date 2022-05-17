from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(prefix='categorys', viewset=views.CategoryViewSet, basename='category')
router.register(prefix='buses', viewset=views.BusViewSet, basename='buses')
router.register(prefix='seats', viewset=views.SeatViewSet, basename='seats')
router.register(prefix='routes', viewset=views.RouteViewSet, basename='routes')
router.register(prefix='ticketbookings', viewset=views.TicketbookingViewSet, basename='ticketbooking')
router.register(prefix='users', viewset=views.UserViewSet, basename='user')
router.register(prefix='comments', viewset=views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),     
]