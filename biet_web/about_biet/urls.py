from django.urls import path

from . import views

urlpatterns = [
    path('Bapuji_educational_association',views.Bapuji_educational_association, name='Bapuji_educational_association'),
    path('Vision_Mission_Quality_Policies',views.Vision_Mission_Quality_Policies, name='Vision_Mission_Quality_Policies'),
    path('academic_calender',views.academic_calender, name='academic_calender'),
    path('governing_body',views.governing_body, name='governing_body'),
    path('major_events',views.major_events, name='major_events'),
    path('nirf',views.nirf, name='nirf'),
    path('nain',views.nain, name='nain'),
    path('naac',views.naac, name='naac'),
    path('aicte',views.aicte, name='aicte'),
    path('nba',views.nba, name='nba'),
    path('director_msg',views.director_msg, name='director_msg'),
    path('principal_msg',views.principal_msg, name='principal_msg'),
]