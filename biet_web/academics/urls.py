from django.urls import path

from . import views

urlpatterns = [
    # path('Bapuji_educational_association',views.Bapuji_educational_association, name='Bapuji_educational_association'),
    path('library',views.library, name='library'),
    path('academic_calender',views.academic_calender, name='academic_calender'),
    path('ranks',views.ranks, name='ranks'),
    path('library/layout',views.layout, name='layout'),
    path('library/staff',views.staff, name='staff'),
    path('library/resources',views.resources, name='resources'),
    path('library/membership',views.membership, name='library/membership'),
    path('library/rules',views.rules, name='library/rules'),
    path('library/services',views.services, name='library/services'),
    path('library/e_resources',views.e_resources, name='library/e_resources'),
    path('library/committee',views.committee, name='library/committee'),
    path('library/question_papers',views.question_papers, name='library/question_papers'),
    path('library/online_courses',views.online_courses, name='library/online_courses'),
    path('library/gallery',views.gallery, name='library/gallery'),
    path('library/user_manual',views.user_manual, name='library/user_manual'),
    # path('major_events',views.major_events, name='major_events'),
]