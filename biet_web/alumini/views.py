from django.shortcuts import render

# Create your views here.
def alumni_association(request):
    return render(request,'alumini/alumni_association.html')

def associationmember(request):
    return render(request,'alumini/associationmember.html')

def alumni_registration(request):
    return render(request,'alumini/alumni_registration.html')

def alumnilogin(request):
    return render(request,'alumini/alumnilogin.html')
