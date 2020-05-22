from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('gallery',views.gallery, name='gallery'),
    path('allevent',views.allevent, name='allevent'),
    path('home',views.home, name='home')
    
]