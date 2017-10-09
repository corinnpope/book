from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Resource, Favorite


def index(request):
	latest_resource_list = Resource.objects.all()
	context = {'latest_resource_list':latest_resource_list}
	return render(request, 'index.html', context)

def detail(request, resource_id):
	# return HttpResponse("You're looking at resource %s." %resource_id)
	try:
		resource = Resource.objects.get(pk=resource_id)
		context = {'resource': resource}
	except Question.DoesNotExist:
		raise Http404("Resource does not exist")
	return render(request, 'detail.html', context)

def favorites(request, resource_id):
	# favorites = "You're looking at the favorites and comments of resource %s."
	# return HttpResponse(favorites %resource_id)
	try:
		resource = Resource.objects.get(pk=resource_id)
		context = {'resource': resource}
	except Question.DoesNotExist:
		raise Http404("Resource does not exist")
	return render(request, 'favorites.html', context)

def vote(request, resource_id):
	return HttpResponse("You're voting on resource %s." %resource_id)


