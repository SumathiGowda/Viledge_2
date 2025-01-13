from django import forms
from .models import Complaint  # Assuming you will create the Complaint model in the next step

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint  # This will refer to the model you define in models.py
        fields = ['name', 'phone', 'location', 'department', 'address', 'complaint']  # Fields to display in the form
