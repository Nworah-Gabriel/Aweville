from django.contrib import admin
from .models import Message, Booking, Subscriber, Room

# Register your models here.
admin.site.register(Message)
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(Subscriber)