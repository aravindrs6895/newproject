from django import forms
from . models import movie1
class movieform(forms.ModelForm):
    class Meta:
        model=movie1
        fields=['name','year','des','image']