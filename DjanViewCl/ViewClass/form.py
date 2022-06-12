from django import forms

class Someform(forms.Form):
    name = forms.CharField(max_length=255)
    nickname = forms.CharField(max_length=255)