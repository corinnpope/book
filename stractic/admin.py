from django.contrib import admin

# Register your models here.
from .models import Resource, Favorite

admin.site.register(Resource)
admin.site.register(Favorite)

class ResourceAdmin(admin.ModelAdmin):
	fields = ('resource_name', 'resource_url', 'resource_description')
	pass
