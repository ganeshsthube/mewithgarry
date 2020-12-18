
#CCNA,CSE,CCDA

from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages


# Create your views here.
def just(request):
    return render(request,"index.html")

def links(request):
    return HttpResponse("This is my link") 

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        Desc = request.POST.get("desc")
        contact = Contact(name = name,email = email, phone = phone, Desc = Desc, date = datetime.today())
        contact.save()
        messages.success(request,"Data save to database successfully")
    return render(request,"contact.html")       
