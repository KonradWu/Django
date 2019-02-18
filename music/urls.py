from django.urls import path
from django.conf.urls import include, url
from . import views
#to jest z tego katalogu


urlpatterns = [
    url('^$', views.index, name='index'),
]