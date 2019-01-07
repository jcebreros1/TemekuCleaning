from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('management/', views.management, name='management'),
    path('services/', views.services, name='services'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('blog/', views.blog, name='blog'),
    path('contactus/', views.contactus, name='contactus'),
    path('houseservices/', views.houseservices, name='houseservices'),
    path('officeservices/', views.officeservices, name='officeservices'),
]