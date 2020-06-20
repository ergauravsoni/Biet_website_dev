from django.shortcuts import render
from .models import Academic_Calender, Office_Staff,EOA

# Create your views here.
def Bapuji_educational_association(request):
    return render(request,'about_biet/Bapuji_educational_association.html')

def Vision_Mission_Quality_Policies(request):
    return render(request,'about_biet/bietHome.html')

def academic_calender(request):
    academic_calender = Academic_Calender.objects.all()
    return render(request,'about_biet/academic_calender.html',{'academic_calender' : academic_calender})

def governing_body(request):
    return render(request,'about_biet/governing_body.html')

def major_events(request):
    return render(request,'about_biet/major_events.html')

def nba(request):
    return render(request,'about_biet/nba.html')

def nain(request):
    return render(request,'about_biet/nain.html')

def naac(request):
    return render(request,'about_biet/naac.html')

def nirf(request):
    return render(request,'about_biet/nirf.html')

def director_msg(request):
    return render(request,'about_biet/director_msg.html')

def principal_msg(request):
    return render(request,'about_biet/principal_msg.html')

def chairman_msg(request):
    return render(request,'about_biet/chairman_msg.html')

def office(request):
    office_member_data = Office_Staff.objects.all().order_by('sno')
    return render(request,'about_biet/office.html',{'office_member_data' : office_member_data})
def aicte(request):
    eoas = EOA.objects.all()
    return render(request,'about_biet/aicte.html')
