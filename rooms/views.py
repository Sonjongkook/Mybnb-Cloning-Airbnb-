from django.utils import timezone
from django.views.generic import ListView
from . import models
from django.shortcuts import render


class HomeView(ListView):
    # Home view definition
    model = models.Room
    paginate_by = 10	
    ordering = "created"
    paginate_orphans = 5	
    page_kwarg = 'page'	
    context_object_name = "rooms"


def room_detail(request, pk):
    print(pk)

    return render(request, "rooms/detail.html")

