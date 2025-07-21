from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail,EmailMultiAlternatives
from mysite.forms import ContactForm
from service.models import Service
from django.core.paginator import Paginator
from mysite import views
from django.conf import settings


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,'service.html')

def interior(request):
    return render(request,'interior.html')

def residential(request):
    return render(request,'residential.html')

def commercial(request):
    return render(request,'commercial.html')

def architectural(request):
    return render(request,'architectural.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contactNumber = form.cleaned_data['contactNumber']
            subject = f"Contact Us Form: {form.cleaned_data['subject']}"
            message=form.cleaned_data['message']
            email= form.cleaned_data['email']

            full_message = f"From: {name} <{email}>\n\n{message}"

            send_mail(
                subject,
                full_message,
                None,
                ['jangirsunidhi@gmail.com'], # The email address to send the contact form submission to
                fail_silently=False,
            )
        
            return render(request, "contact.html",{
                'form':ContactForm(), 
                'success': True,
                'name': name
            })
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})
    