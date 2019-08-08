from django.conf.urls import url
from .views import IndexView, DetailView, AlbumCreate, AlbumUpdate, AlbumDelete, UserFormView, SongCreate

app_name = 'music'

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^register/$', UserFormView.as_view(), name='register'),
	url(r'^(?P<pk>\d+)/$', DetailView.as_view(), name='detail'),
	url(r'^album/add/$', AlbumCreate.as_view(), name='album-add'),
	url(r'^album/(?P<pk>\d+)/$', AlbumUpdate.as_view(), name='album-update'),
	url(r'^album/(?P<pk>\d+)/delete/$', AlbumDelete.as_view(), name='album-delete'),
	url(r'^song/add$', SongCreate.as_view(), name='song-add'),	
]