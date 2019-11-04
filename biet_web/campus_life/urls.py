from django.urls import path

from . import views

urlpatterns = [
    path('campus_life/naac',views.naac, name='naac'),
    path('campus_life/nirf',views.nirf, name='nirf'),
    path('to_be_updated',views.to_be_updated, name='to_be_updated'),
    path('campus_life/nain',views.nain, name='nain'),
    path('campus_life/graduation_day',views.graduation_day, name='graduation_day'),
]