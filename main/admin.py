from django.contrib import admin
from .models import Task, Guest
# Register your models here.
admin.site.register(Guest)
admin.site.register(Task)