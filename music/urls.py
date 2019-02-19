from django.urls import path
from django.conf.urls import include, url
from . import views
#to jest z tego katalogu

app_name = 'music'

urlpatterns = [
    # /music/
    url('^$', views.index, name='index'),

    # /music/721/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'), #album_id złożone z cyfr
]