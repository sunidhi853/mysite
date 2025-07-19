from django.db import models

class Service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_des = models.TextField()
    service_img = models.FileField(upload_to='serviced/', max_length=250,null=True,default=None)

class contactEnquiry(models.Model):
    name = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    subject = models.CharField(max_length=70)
    message = models.TextField()

