from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request, 'index.html')

def SignInView(request):
    return render(request, 'signin.html')

def RegisterView(request):
    return render(request, 'register.html')
