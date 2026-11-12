from django.urls import path
from customer import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about_us",views.about_us,name="about_us"),
    path("services",views.services,name="services"),
    path("customers",views.customers,name="customers"),
    path("accounts",views.accounts,name="accounts"),
    path("loan",views.loan,name="loan"),
    path("contact",views.contact,name="contact"),
]