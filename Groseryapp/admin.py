from django.contrib import admin
from .models import UserProfile
from Groseryapp.models import *
# Register your models here.
#admin.site.register(Student)
admin.site.register(Carousel)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(Booking)
admin.site.register(Feedback)