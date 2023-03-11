from django.shortcuts import render
from .models import Bb


def index(request):
    bbs = Bb.objects.order_by('-published')
    return render(request, 'first_app/index.html', {'bbs': bbs})
