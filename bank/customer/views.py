from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def about_us(request):
    return render(request,"about_us.html")
def services(request):
    return render(request,"services.html")
def customers(request):
    return render(request,"customers.html")
def accounts(request):
    return render(request,"accounts.html")
def loan(request):
    return render(request,"loan.html")
def contact(request):
    return render(request,"contact.html")