from django.conf.urls import url
from  . import views

app_name = 'music'

urlpatterns = [
    url(r'^yah', views.jab, name='jab'),
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^(\d+)/favorite/$', views.favorite, name='favorite'),
    url(r'^add_new_album', views.add_new_album, name='add_new_album'),
    url(r'^add_new_song', views.add_new_song, name='add_new_song'),
]