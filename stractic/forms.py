from django import forms
from .models import Resource, Favorite

class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resource
        fields = ('resource_name', 'resource_url', 'resource_description')

class FavoriteForm(forms.ModelForm):

    class Meta:
        model = Favorite
        fields = ('favorited', 'comments', 'votes')