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
    path('chairman_msg',views.chairman_msg, name='chairman_msg'),
    path('deans',views.deans, name='deans'),
    path('office',views.office, name='office'),
    path('research',views.research, name='research'),
    path('research/dean_message',views.dean_message, name='research/dean_message'),
    path('research/recognized_research_centers',views.recognized_research_centers, name='research/recognized_research_centers'),
    path('research/funded_projects',views.funded_projects, name='research/funded_projects'),
    path('research/kscst_projects',views.kscst_projects, name='research/kscst_projects'),
    path('research/industry_collaboration',views.industry_collaboration, name='research/industry_collaboration'),
    path('research/product_development',views.product_development, name='research/product_development'),
    path('research/research_facilities',views.research_facilities, name='research/research_facilities'),
    path('research/honors_and_awards',views.honors_and_awards, name='research/honors_and_awards'),
    path('other_committees/grievance_redressal',views.grievance_redressal, name='other_committees/grievance_redressal'),
    path('other_committees/anti_ragging',views.anti_ragging, name='other_committees/anti_ragging'),
]
