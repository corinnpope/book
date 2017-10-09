from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
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
	except resource.DoesNotExist:
		raise Http404("Resource does not exist")
	return render(request, 'detail.html', context)

def favorites(request, resource_id):
	try:
		resource = Resource.objects.get(pk=resource_id)
		context = {'resource': resource}
	except resource.DoesNotExist:
		raise Http404("Resource does not exist")
	return render(request, 'favorites.html', context)

def vote(request, resource_id):
	resource = get_object_or_404(Resource, pk=resource_id)
	try:
		selected_favorite = resource.favorite_set.get(pk=request.POST['favorite'])
	except (KeyError, Favorite.DoesNotExist):
	# Redisplay the resource voting form.
		return render(request, 'stractic/detail.html', {
			'resource': resource,
			'error_message': "You didn't fav it",
			})
	else:
		selected_favorite.votes += 1
		selected_favorite.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('stractic:results', args=(resource.id,)))


def results(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    return render(request, 'stractic/results.html', {'resource': resource})