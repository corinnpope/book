from django.conf.urls import include, url

from . import views

app_name = 'stractic'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<resource_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<resource_id>[0-9]+)/favorites/$',views.favorites,name='favorites'),
    url(r'^(?P<resource_id>[0-9]+)/vote/$',views.vote,name='vote'),
    url(r'^(?P<resource_id>[0-9]+)/results/$',views.results,name='results'),
    url(r'^new', views.resource_new, name='resource_new'),
    url(r'^(?P<resource_id>[0-9]+)/resource_edit/$', views.resource_edit, name='resource_edit'),
    url(r'^(?P<resource_id>[0-9]+)/edit_fav/$',views.edit_fav, name='edit_fav'),
]