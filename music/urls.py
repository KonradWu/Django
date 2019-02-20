from django.conf.urls import include, url
from . import views
#to jest z tego katalogu

app_name = 'music'

urlpatterns = [
    # /music/
    url('^$', views.IndexView.as_view(), name='index'),

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]