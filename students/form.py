from django import forms
import students

from students.models import student



class StudentForm(forms.ModelForm):

    class Meta:

        model=student

        fields="__all__"