from django.urls import path
from patient import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("services/",views.services,name="services"),
    path("doctors/",views.doctors,name="doctors"),
    path("contact/",views.contact,name="contact"),
     path("book_appoinment",views.book_appoinment,name="book_appoinment")
]
