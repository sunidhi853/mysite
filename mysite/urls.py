"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views
from django.conf import settings  # <-- Add this import
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'), 
    path('residential/', views.residential, name='residential'), 
    path('commercial/', views.commercial, name='commercial'),  
    path('interior/', views.interior, name='interior'), 
    path('architectural/', views.architectural, name='architectural'),
    path('contact/' , views.contact, name='contact'),
    # path('contactEnquiry/', views.saveEnquiry, name='save_enquiry'),
    path('calculator/', views.calculator, name='calculator'),
    path('newsDetails/<newsid>',views.calculator),
    
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)