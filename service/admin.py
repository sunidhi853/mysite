from django.contrib import admin
from service.models import Service
from service.models import contactEnquiry

class serviceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des','service_img')

admin.site.register(Service, serviceAdmin)

class contactEnquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','contactNumber','subject','message')

admin.site.register(contactEnquiry,contactEnquiryAdmin)
# Register your models here.
