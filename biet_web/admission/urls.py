from django.urls import path

from . import views

urlpatterns = [
    path('ug_addmission',views.ug_addmission, name='ug_addmission'),
    path('pg_addmission',views.pg_addmission, name='pg_addmission'),
    path('reserach',views.reserach, name='reserach'),
]