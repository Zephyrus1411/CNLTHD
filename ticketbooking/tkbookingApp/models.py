from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(null=True, upload_to='users/%Y/%m')
    
class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(ModelBase):
    type = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.type
    
class Buses(models.Model):
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    bus_name = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.bus_name

class Customers(models.Model):
    cus_name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.cus_name
class Numb(models.Model):
    numb_phone = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.numb_phone

class Seats(models.Model):
    active = models.BooleanField(default=True)
    seat_numb = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.seat_numb

class Routes(ModelBase):
    bus_name = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    begining = models.CharField(max_length=255, null=False)
    destination = models.CharField(max_length=255, null=False)
    cost = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.begining + " to " + self.destination

class Comment(ModelBase):
    content = models.TextField()
    routes = models.ForeignKey( Routes, related_name='comments',  on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
class Ticketbooking(ModelBase):
    cus_name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='picture/%Y/%m')
    numb_phone = models.CharField(max_length=50, unique=True, null = True)
    buses = models.ForeignKey(Buses, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    seats = models.ForeignKey(Seats, null=True, on_delete=models.CASCADE)
    routes = models.ForeignKey(Routes, null=True, on_delete=models.CASCADE)
    note = models.CharField(max_length=50, unique=True, null = True)
# Create your models here.
