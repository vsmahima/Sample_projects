from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def asset_registration(request):
    return render(request,"asset_registration.html")
def asset_allocation(request):
    return render(request,"asset_allocation.html")
def maintenence(request):
    return render(request,"maintenence.html")
def reports(request):
    return render(request,"reports.html")
def login(request):
    return render(request,"login.html")