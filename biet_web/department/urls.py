from django.urls import path

from . import views

urlpatterns = [
    path('department/<str:course>/<str:dept>/home', views.home, name='home'),
]
