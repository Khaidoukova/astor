from django.contrib import admin
from main.models import Company, Office, User_request, Booking, Cars


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_per_page = 10


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('office_id', 'floor', 'sq_m', 'description', 'price')
    list_editable = ['floor', 'sq_m', 'price']
    list_per_page = 10


@admin.register(User_request)
class User_requestAdmin(admin.ModelAdmin):
    list_display = ('date', 'office_id', 'owner', 'description', 'urgency', 'status', 'comments')
    list_per_page = 10


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'duration', 'owner')
    list_per_page = 10


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'model', 'description', 'price', 'owner')
    list_per_page = 10
