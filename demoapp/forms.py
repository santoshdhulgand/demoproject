
from django import forms
from .models import Student


class AddStudentForm(forms.ModelForm):
    class Meta:
        model   = Student
        fields  = '__all__'



class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model   = Student
        fields  = '__all__'