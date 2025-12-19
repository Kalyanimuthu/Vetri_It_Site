from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('web_development/', views.web_development, name='web_development'),
    path('software_development/', views.software_development, name='software_development'),
    path('digital_marketing/', views.digital_marketing, name='digital_marketing'),
    path('about_us/', views.about_us, name='about_us'),
    path("enquiry/", views.enquiry, name="enquiry"),

]
