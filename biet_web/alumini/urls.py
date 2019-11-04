from django.urls import path

from . import views

urlpatterns = [
    path('alumini/alumni_association',views.alumni_association, name='alumni_association'),
    path('alumini/associationmember',views.associationmember, name='associationmember'),
    path('alumini/alumni_registration',views.alumni_registration, name='alumni_registration'),
    path('alumini/alumnilogin',views.alumnilogin, name='alumnilogin'),
]