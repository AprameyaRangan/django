from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def AboutUs(request):
    return render(request,'AboutUs.html')
def product(request):
    return render(request,'product.html')
def service(request):
    return render(request,'service.html')
