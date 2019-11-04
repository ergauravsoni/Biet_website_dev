from django.shortcuts import render
from .models import Sport

# Create your views here.

def sport(request):
    report = Sport.objects.all().order_by('reports')

    result = []

    for i in report:
        # print(i)
        reports_sports = {}
        reports_sports['url'] = str(i)
        reports_sports['title'] = str(i).split('/')[-1].split('.')[0]
        result.append(reports_sports)

    return render(request,'facilities/sport.html',{'result' : result })

def hostel(request):
    return render(request,'facilities/hostel.html')

def canteen(request):
    return render(request,'facilities/canteen.html')

def scholarship(request):
    return render(request,'facilities/scholarship.html')

def medical(request):
    return render(request,'facilities/medical.html')

def perography(request):
    return render(request,'facilities/perography.html')

def internet(request):
    return render(request,'facilities/internet.html')

def transportation(request):
    return render(request,'facilities/transportation.html')

def edusat(request):
    return render(request,'facilities/edusat.html')

def language_lab(request):
    return render(request,'facilities/language_lab.html')



