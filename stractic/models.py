from django.db import models

# Create your models here.

class Resource(models.Model):
	resource_name = models.CharField(max_length=200)
	resource_url = models.CharField(max_length=300)
	resource_description = models.CharField(max_length=2000)

	def __str__(self):
		return self.resource_name

class Favorite(models.Model):
	resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
	favorited = models.BooleanField()
	comments = models.CharField(max_length=280)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.comments