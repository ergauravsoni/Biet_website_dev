from django.shortcuts import render
from .models import Library_User_Manual, Gallary

# Create your views here.

def library(request):
    return render(request,'academics/library.html')

def academic_calender(request):
    return render(request,'aboutacademics_biet/academic_calender.html')

def ranks(request):
    return render(request,'academics/ranks.html')

def layout(request):
    return render(request,'academics/library/layout.html')

def staff(request):
    return render(request,'academics/library/staff.html')

def resources(request):
    return render(request,'academics/library/resources.html')

def membership(request):
    return render(request,'academics/library/membership.html')

def rules(request):
    return render(request,'academics/library/rules.html')

def services(request):
    return render(request,'academics/library/services.html')

def e_resources(request):
    return render(request,'academics/library/e_resources.html')

def committee(request):
    return render(request,'academics/library/committee.html')

def question_papers(request):
    return render(request,'academics/library/question_papers.html')

def online_courses(request):
    return render(request,'academics/library/online_courses.html')

def gallery(request):
    images = Gallary.objects.all()
    return render(request,'academics/library/gallery.html', {'images' : images})

def user_manual(request):
    user_manual = Library_User_Manual.objects.all()
    return render(request,'academics/library/user_manual.html',{'user_manual' : user_manual})

