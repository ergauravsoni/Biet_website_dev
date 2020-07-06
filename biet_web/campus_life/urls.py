from django.urls import path

from . import views

urlpatterns = [
    path('campus_life/naac',views.naac, name='naac'),
    path('campus_life/nirf',views.nirf, name='nirf'),
    path('to_be_updated',views.to_be_updated, name='to_be_updated'),
    path('campus_life/nain',views.nain, name='nain'),
    path('campus_life/green_campus',views.green_campus, name='green_campus'),
    path('campus_life/redcross',views.redcross, name='redcross'),
    path('campus_life/graduation_day',views.graduation_day, name='graduation_day'),
    path('campus_life/btech_technowav',views.btech_technowav, name='btech_technowav'),
]
