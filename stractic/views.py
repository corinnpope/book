from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Resource, Favorite
from .forms import ResourceForm, FavoriteForm
from django.forms import inlineformset_factory


def index(request):
	latest_resource_list = Resource.objects.all()
	context = {'latest_resource_list':latest_resource_list}
	return render(request, 'index.html', context)

def detail(request, resource_id):
	# return HttpResponse("You're looking at resource %s." %resource_id)
	try:
		resource = Resource.objects.get(pk=resource_id)
		context = {'resource': resource}
		FavInlineFormSet = inlineformset_factory(Resource, Favorite, fields=('favorited', 'comments', 'votes',))
		if request.method == "POST":
			formset = FavInlineFormSet(request.POST, request.FILES, instance=resource)
			if formset.is_valid():
				formset.save()
	            # Do something. Should generally end with a redirect. For example:
				return HttpResponseRedirect(reverse('stractic:detail', args=(resource.id,)))
		else:
			formset = FavInlineFormSet(instance=resource)
	except resource.DoesNotExist:
		raise Http404("Resource does not exist")


	return render(request, 'stractic/detail.html', context, {'formset': formset})

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

def resource_new(request):

    if request.method == "POST":
    	form = ResourceForm(request.POST)
    	if form.is_valid():
		    resource = form.save(commit=False)
		    # resource.author = request.user
		    # resource.published_date = timezone.now()
		    resource.save()
		    return redirect('stractic:detail', resource_id=resource.pk)
    else:
    	form = ResourceForm()
    return render(request, 'stractic/resource_edit.html', {'form': form})

def resource_edit(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            resource = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            resource.save()
            return redirect('stractic:detail', resource_id=resource.pk)
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'stractic/resource_edit.html', {'form': form})

def edit_fav(request, resource_id):
	# return HttpResponse("You're looking at resource %s." %resource_id)
	resource = Resource.objects.get(pk=resource_id)
	FavInlineFormSet = inlineformset_factory(Resource, Favorite, fields=('favorited', 'comments', 'votes',))
	if request.method == "POST":
		formset = FavInlineFormSet(request.POST, request.FILES, instance=resource)
		if formset.is_valid():
			formset.save()
            # Do something. Should generally end with a redirect. For example:
			return HttpResponseRedirect(reverse('stractic:detail', args=(resource.id,)))
	else:
		formset = FavInlineFormSet(instance=resource)

	return render(request, 'stractic/edit_fav.html', {'formset': formset})