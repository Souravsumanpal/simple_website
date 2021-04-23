from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
    #return HttpResponse("This is homepage")    #URL dispatching

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is aboutpage")

def courses(request):
    return render(request, 'courses.html')
    #return HttpResponse("This is servicespage")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("This is contactpage")            

def login(request):
    return render(request, 'login.html')