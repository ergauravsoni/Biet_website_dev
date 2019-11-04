from django.shortcuts import render
from .models import Placement_Invitaton_For_Company, Placement_Brochure, Gallary

# Create your views here.

def objectives(request):
    return render(request,'placement/objectives.html')

def placement(request):
    return render(request,'placement/placement.html')

def training_program(request):
    return render(request,'placement/training_program.html')

def visitingCompanies(request):
    return render(request,'placement/visitingCompanies.html')

def invitationForCompanies(request):
    invitations = Placement_Invitaton_For_Company.objects.all()
    return render(request,'placement/invitationForCompanies.html',{'invitations' : invitations})

def placementBrochure(request):
    brochures = Placement_Brochure.objects.all()
    return render(request,'placement/placementBrochure.html',{'brochures' : brochures})

def recruit(request):
    images = Gallary.objects.all()
    return render(request,'placement/recruit.html',{'images' : images})

def message(request):
    return render(request,'placement/message.html')
