from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home.as_view(),name="home"),
    path('about', views.About.as_view(), name="about"),
    path('contact', views.Contact.as_view(), name="contact"),
    path('project', views.Project.as_view(), name="project"),
    path('service', views.Service.as_view(), name="service"),
    path('team', views.Team.as_view(), name="team"),
    path('testimonial', views.Testimonial.as_view(), name="testimonial"),


]