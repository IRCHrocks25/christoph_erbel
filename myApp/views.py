from django.shortcuts import render

def home(request):
    return render(request, 'myApp/landing_new.html')