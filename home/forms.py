from django.forms import ModelForm
from .models import Enquiry

class EnquiryForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = ["name","phone","email","message"]