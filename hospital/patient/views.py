from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def doctors(request):
    return render(request,"doctors.html")
def contact(request):
    return render(request,"contact.html")
def book_appoinment(request):
    return render(request,"book_appoinment.html")