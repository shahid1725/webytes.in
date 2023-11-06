from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.


from django.views.generic import TemplateView, CreateView, ListView,DetailView
from .models import Enquiry
from .forms import EnquiryForm

# Create your views here.



class Home(TemplateView):
    template_name = "index.html"

class About(TemplateView):
    template_name = "about.html"

class Contact(CreateView):
    template_name = "contact.html"
    model = Enquiry
    form_class = EnquiryForm
    success_url = reverse_lazy("home")

class Project(TemplateView):
    template_name = "project.html"

class Service(TemplateView):
    template_name = "service.html"

class Team(TemplateView):
    template_name = "team.html"

class Testimonial(TemplateView):
    template_name = "testimonial.html"



