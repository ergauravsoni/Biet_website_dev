from django.urls import path

from . import views

urlpatterns = [
    path('facilities/sport',views.sport, name='sport'),
    path('facilities/auditorium',views.auditorium, name='auditorium'),
    path('facilities/hostel',views.hostel, name='hostel'),
    path('facilities/ladies_rest_room',views.ladies_rest_room, name='ladies_rest_room'),
    path('facilities/canteen',views.canteen, name='canteen'),
    path('facilities/scholarship',views.scholarship, name='scholarship'),
    path('facilities/dispensary',views.dispensary, name='dispensary'),
    path('facilities/perography',views.perography, name='perography'),
    path('facilities/internet',views.internet, name='internet'),
    path('facilities/transportation',views.transportation, name='transportation'),
    path('facilities/elearning',views.elearning, name='elearning'),
    path('facilities/language_lab',views.language_lab, name='language_lab'),
]