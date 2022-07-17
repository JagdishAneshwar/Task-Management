from django.contrib import admin
from .models import member, task

# Register your models here.
admin.site.register(member)
admin.site.register(task)