from django.urls import path, include
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('photo/', views.photo_view, name="photo_view"),
    path('takePhoto/', views.take_photo, name="take_photo")
    ]