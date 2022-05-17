from django.contrib import admin
from django.template.response import TemplateResponse
from .models import Category, Buses, Customers, Routes, Ticketbooking, Seats, User
from django import forms
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path

class TicketbookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'cus_name', 'created_date', 'numb_phone', 'buses', 'category' , 'seats', 'routes']
    search_fields = [ 'buses', 'created_date']
    readonly_fields = ['avatar']
    
    def avatar(self, ticketbooking):
        if ticketbooking:
            return mark_safe(
                    '<img src="/static/{img_url}" width="120" />' \
                        .format(img_url = ticketbooking.image.name)
                )  



admin.site.register(User)
admin.site.register(Category)
admin.site.register(Buses)
admin.site.register(Routes)
admin.site.register(Ticketbooking, TicketbookingAdmin)
admin.site.register(Seats)
# Register your models here.
