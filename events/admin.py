from django.contrib import admin
from .models import TypeOfEvent,Events,User
# Register your models here.

admin.site.register(TypeOfEvent)
admin.site.register(Events)
admin.site.register(User)