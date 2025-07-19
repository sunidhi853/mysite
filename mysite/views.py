from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail,EmailMultiAlternatives
from mysite.forms import ContactForm
from service.models import Service
from django.core.paginator import Paginator
from service.models import contactEnquiry
from mysite import views
from django.conf import settings


def home(request):
    # send_mail(
    #     'Testing mail',
    #     'here is the message',
    #     'jangirsunidhi@gmail.com',
    #     ['jangirsunidhi@gmail.com'],
    #     fail_silently=False,
    # )
    
    # serviceData = Service.objects.all()
    # data={
    #     'serviceData' : serviceData
    # }
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
            subject = f"Contact Us Form: {form.cleaned_data['subject']}"
            message=form.cleaned_data['message']
            email= form.cleaned_data['email']

            full_message = f"From: {name} <{email}>\n\n{message}"

            send_mail(
                subject,
                full_message,
                'jangirsunidhi@gmail.com',
                ['jangirsunidhi@gmail.com'], # The email address to send the contact form submission to
                fail_silently=False,
            )
        
            return render(request, "contact.html", {'form':ContactForm(), 'succes': True })
        else:
            print(form.errors)
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})
    # return render(request,'contact.html')
# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         contactNumber = request.POST['contactNumber']
#         message =request.POST['message']
#         send_mail(
#            'ContactForm',
#             message,
#             ['jangirsunidhi@gmail.com'], # The email address to send the contact form submission to
#             fail_silently=False,
#           )
#         return render(request,'contact.html', {'form': form})
#     else:
#         return render(request,'contact.html')

# def saveEnquiry(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         contactNumber = request.POST.get('contactNumber')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         en = contactEnquiry(name=name, contactNumber=contactNumber,email=email,subject=subject,message=message)
#         en.save()
#     return render(request,'contact.html')

# def contact(request):
#     if request.method =='POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             contactNumber = form.cleaned_data['contactNumber']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             full_message = f"From: {name}<email>\n\n {message}"

#             send_mail(
#                 subject,
#                 full_message,
#                 ['jangirsunidhi@gmail.com'],
#                 fail_silently=False,
#             )
#             return render(request,'contact.html')
#         else:
#             form = ContactForm()
#     return render(request, 'contact.html',{'form': form})




# def calculator(request):
#     c =''
#     try:
#         if request.method == "POST":
#             n1 = eval(request.POST.get('val1'))
#             n2 = eval(request.POST.get('val2'))
#             opr = request.POST.get('opr')
#             if opr == "+":
#                 c = n1+n2
#             elif opr == "-":
#                 c =n1 - n2
#             elif opr == "*":
#                 c =n1 * n2
#             elif opr == "/":
#                 c =n1 / n2
#     except:
#         pass
#     print(c)
#     return render(request, 'calculator.html', {'c': c})

# def calculator(request):
#     c = ''
#     try:
#         if request.method == 'POST':
#             num = int(request.POST.get('num'))
#             if num%2 == 0:
#                 c ='even number'
#             else:
#                 c = 'odd number'
#     except:
#         pass
#     return render(request, 'calculator.html', {'c': c})
# def calculator(request):
#     if request.method == 'POST':
#         if request.POST.get('sub1') == "":
#             return render(request,'calculator.html', {'error': True})
#         s1 = eval(request.POST.get('sub1'))
#         s2 = eval(request.POST.get('sub2'))
#         s3 = eval(request.POST.get('sub3'))
#         s4 = eval(request.POST.get('sub4'))
#         t = s1+s2+s3+s4
#         per = t*100/400
#         if per >80:
#             d = 'first division'
#         elif per>50 and per<80:
#             d ='second division'
#         elif per>30 and per<60:
#             d ='thierd division'
#         else:
#             d ='fail'
#         data ={
#             'total': t,
#             'per1': per,
#             'divi': d
#         }
#         return render(request, 'calculator.html',data )
def calculator(request):
    serviceData = Service.objects.all()
    if request.method == "GET":
        st = request.GET.get('name1')
        if st != None:
            serviceData = Service.objects.filter(service_title__icontains=st)
    data2={
        'serviceData' : serviceData
    }
    return render(request, 'calculator.html', data2)

# def newsDetails(request, newsid):
#     newsDetails = Service.objects.get(id=newsid)
#     data1={
#         'newsDetails': newsDetails
#     }
#     return render(request, 'calculator.html', data1)

def calculator(request):
    ServiceData = Service.objects.all()
    paginator = Paginator(ServiceData,1)
    page_number = request.GET.get('page')
    pageFinal = paginator.get_page(page_number)
    totalPage = pageFinal.paginator.num_pages
    data={
        'pageFinal': pageFinal,
        'LastPage': totalPage,
        'pageList' : [n for n in range(totalPage)]
    }
    return render(request,'calculator.html',data)

# def newsDetails(request):
#     newsid = request.GET.get('id')  # Get the ID from the query parameters
#     print(f"Requested ID: {newsid}")  # Debugging line to check if ID is correct
#     newsDetails = None

#     if newsid:
#         try:
#             # Try to fetch the newsDetails based on the ID
#             newsDetails = Service.objects.get(id=newsid)
#             print(f"Fetched newsDetails: {newsDetails}")  # Debugging line to check if object is fetched
#         except Service.DoesNotExist:
#             print(f"Service with ID {newsid} does not exist.")  # Debugging line for non-existent object
#             newsDetails = None

#     if newsDetails:
#         return render(request, 'calculator.html', {'newsDetails': newsDetails})
#     else:
#         return render(request, 'error.html', {'message': 'Service not found or invalid ID.'})
