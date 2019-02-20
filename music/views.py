from django.views import generic
from .models import  Album


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'object_list' #ta nazwa jest z automatu i w index.html ale możemy zmienić na inną jeśli chcemy to właśnie w tym miejscu

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
