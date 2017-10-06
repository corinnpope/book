from django.conf.urls import include, url

from . import views

app_name = 'stractic'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<resource_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<resource_id>[0-9]+)/favorites/$',views.favorites,name='favorites'),
    url(r'^(?P<resource_id>[0-9]+)/vote/$',views.vote,name='vote'),
]
