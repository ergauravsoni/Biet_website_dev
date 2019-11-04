from django.shortcuts import render
from .models import UG_addmission, PG_addmission

# Create your views here.
def ug_addmission(request):
    addmissions = UG_addmission.objects.all()
    return render(request,'admission/ug_addmission.html', {'addmissions' : addmissions})

def pg_addmission(request):
    addmissions = PG_addmission.objects.all()
    return render(request,'admission/pg_addmission.html', {'addmissions' : addmissions})

def reserach(request):
    return render(request,'admission/research.html')
