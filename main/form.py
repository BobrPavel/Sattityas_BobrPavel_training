from django import forms

class CreateEmailForms(forms.Form):

    email = forms.CharField()