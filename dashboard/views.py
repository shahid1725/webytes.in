from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from . import forms

# Create your views here.


class Login(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        context = {"form": form}
        return render(request, "login.html", context)

    def post(self,request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if (user):
                login(request, user)
                return redirect("dashboard")

            else:
                return render(request, "login.html", {"form": form})

def signout(request):
    logout(request)
    return redirect("login")

class Dashboard(TemplateView):
    template_name = "dashboard.html"

def base(request):
    return render(request,"base.html")









#------------------------------ ENQUIRIES-------------------------------
from home.models import Enquiry
from .forms import EnquiryUpdateForm
class ListEnquiryView(ListView):
    template_name = "enquiries.html"
    model = Enquiry
    context_object_name = "enquiries"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        enquiries = self.model.objects.all()
        context["enquiries"] = enquiries
        return context

class ListAttendedEnquiryView(ListView):
    template_name = "attended_enquiries.html"
    model = Enquiry
    context_object_name = "attendedenq"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        attendedenq = self.model.objects.filter(status="Attended")
        context["attendedenq"] = attendedenq
        return context

class EditEnquiryView(UpdateView):
    template_name = "enquiry_edit.html"
    model = Enquiry
    form_class = EnquiryUpdateForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("enquiries")

    # def get_object(self, queryset=None):
    #     return Enquiry.objects.get(name=self.kwargs['id'])
