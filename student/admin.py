from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(EventModel)
admin.site.register(OrderEvent)
admin.site.register(Order)
admin.site.register(Profile)

