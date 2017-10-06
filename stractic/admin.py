from django.contrib import admin

# Register your models here.
from .models import Resource, Favorite

admin.site.register(Resource)
admin.site.register(Favorite)