from django.http import HttpResponse
from django.shortcuts import render
from picamera import PiCamera
from time import sleep
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def photo_view(request):
    return render(request, 'main/photo.html')


def take_photo(request):
	camera = PiCamera()
	camera.rotation = 180
	file_name = datetime.now().strftime('%Y_%m_%d_%Hh%Mm%Ss')
	camera.start_preview()
	sleep(3)
	camera.capture(f'./main/static/main/images/{file_name}.jpg')
	camera.stop_preview()
	camera.close()

	return HttpResponse(file_name)
