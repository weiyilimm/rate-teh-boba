from django.shortcuts import render

def home(request):
    return render(request,'rating/home.html')

def about(request):
    return render(request,'rating/about.html',{'title':'about'})

def contact(request):
    return render(request,'rating/contact.html',{'title':'Contact-Us'})
