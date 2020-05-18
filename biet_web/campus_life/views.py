from django.shortcuts import render
from .models import Graduation_Day, NAAC

# Create your views here.
def naac(request):
    brochures = NAAC.objects.all()
    return render(request,'campus_life/naac.html',{'brochures' : brochures})

def nirf(request):
    return render(request,'campus_life/nirf.html')



def nain(request):
    return render(request,'campus_life/nain.html')

def graduation_day(request):
    images = Graduation_Day.objects.all()
    print(images)
    return render(request,'campus_life/graduation_day.html',{'images' : images})


def to_be_updated(request):
    return render(request, 'to_be_updated.html')

def redcross(request):
    return render(request, 'campus_life/redcross.html')
