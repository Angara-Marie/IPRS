from models import Customer
from django.forms import ModelForm

#creating a Meta class
class CustomerRegistrationForm(ModelForm):
    class Meta:
        model=Customer
        fields="__all__"