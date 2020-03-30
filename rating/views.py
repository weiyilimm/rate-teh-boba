from django.shortcuts import render

def home(request):
    return render(request,'rating/home.html')

def about(request):
    return render(request,'rating/about.html')
