from django.urls import path
from django.conf.urls import include, url
from . import views
#to jest z tego katalogu


urlpatterns = [
    # /music/
    url('^$', views.index, name='index'),

    # /music/album_id
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'), #album_id złożone z cyfr
]