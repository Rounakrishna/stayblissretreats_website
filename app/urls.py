from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.ABOUT,name='home'),
    path('about/',views.ABOUT,name='about'),
    path('contact/',views.CONTACT,name='contact'),
    path('gallery',views.GALLERY,name='gallery'),
    path('package',views.PACKAGE,name='package'),
    path('carrer',views.CARRER,name='carrer'),
    path('testimonial',views.TESTIMONIAL,name='testimonial'),


]




