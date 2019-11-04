from django.urls import path

from . import views

urlpatterns = [
    path('facilities/sport',views.sport, name='sport'),
    path('facilities/hostel',views.hostel, name='hostel'),
    path('facilities/canteen',views.canteen, name='canteen'),
    path('facilities/scholarship',views.scholarship, name='scholarship'),
    path('facilities/medical',views.medical, name='medical'),
    path('facilities/perography',views.perography, name='perography'),
    path('facilities/internet',views.internet, name='internet'),
    path('facilities/transportation',views.transportation, name='transportation'),
    path('facilities/edusat',views.edusat, name='edusat'),
    path('facilities/language_lab',views.language_lab, name='language_lab'),
]