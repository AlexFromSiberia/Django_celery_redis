from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Subscription email form"""
    class Meta:
        model = Contact
        fields = "__all__"

