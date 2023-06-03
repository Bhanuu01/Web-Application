from django.contrib import admin
from .models import resource

class ResourceAdmin(admin.ModelAdmin):
    list_display=("desc","img")

admin.site.register(resource)

# Register your models here.
