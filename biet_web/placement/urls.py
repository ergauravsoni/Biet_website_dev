from django.urls import path

from . import views

urlpatterns = [
    path('placement/objectives',views.objectives, name='objectives'),
    path('placement/placement',views.placement, name='placement'),
    path('placement/training_program',views.training_program, name='training_program'),
    path('placement/visitingCompanies',views.visitingCompanies, name='visitingCompanies'),
    path('placement/invitationForCompanies',views.invitationForCompanies, name='invitationForCompanies'),
    path('placement/placementBrochure',views.placementBrochure, name='placementBrochure'),
    path('placement/recruit',views.recruit, name='recruit'),
    path('placement/message',views.message, name='message'),
]