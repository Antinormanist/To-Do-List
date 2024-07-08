from django import forms

class CreateTask(forms.Form):
    text = forms.CharField()
    name = forms.CharField()