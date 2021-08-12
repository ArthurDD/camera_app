from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def photo_view(request):
    return render(request, 'main/photo.html')


def take_photo(request):

    name = 'Blabla'
    return HttpResponse(name)
