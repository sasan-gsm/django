from django.shortcuts import get_object_or_404, render
from django.template import loader, RequestContext
from django.http.response import HttpResponse

from .models import Tag, Startup


def homepage(resuest):
    return render(resuest, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'organizer/tag_detail.html', {'tag': tag})


def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})


def startup_list(request):
    return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})


def startup_detail(request):
    return render(request, 'organizer/startup_detail.html', {'startup': Startup})
