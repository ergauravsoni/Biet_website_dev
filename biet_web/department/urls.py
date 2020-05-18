from django.urls import path

from . import views

urlpatterns = [
    path('department/<str:course>/<str:dept>/achievements',
         views.achievements, name='achievements'),
    path('department/<str:course>/<str:dept>/activities',
         views.activities, name='activities'),
    path('department/<str:course>/<str:dept>/faculty',
         views.faculty, name='faculty'),
    path('department/<str:course>/<str:dept>/gallery',
         views.gallery, name='gallery'),
    path('department/<str:course>/<str:dept>/home', views.home, name='home'),
    path('department/<str:course>/<str:dept>/infrastructure',
         views.infrastructure, name='infrastructure'),
    path('department/<str:course>/<str:dept>/profile',
         views.profile, name='profile'),
    path('department/<str:course>/<str:dept>/research',
         views.research, name='research'),
    path('department/<str:course>/<str:dept>/psopso',
         views.psopso, name='psopso'),
    path('department/<str:course>/<str:dept>/newsletter',
         views.newsletter, name='newsletter'),
]
