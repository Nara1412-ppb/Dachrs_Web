from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request , 'home.html')

def Contact(request):
    return render(request , 'contactus.html')

def About(request):
    return render(request , 'aboutus.html')

def Products(request):
    return render(request , 'products.html')

def Sales(request):
    return render(request , 'sales.html')

def Services(request):
    return render(request , 'services.html')

