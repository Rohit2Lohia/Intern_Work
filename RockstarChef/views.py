from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')
    #return HttpResponse("Home Page!!  Its cool here.")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("About")
