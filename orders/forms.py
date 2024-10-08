from django import forms

class CreateOrderForms(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    company_name = forms.CharField(required=False)
    delivery_address = forms.CharField()
    city = forms.CharField()
    index_cod = forms.CharField()
    phone_number = forms.CharField()
    email = forms.CharField()
    additional_inforation = forms.CharField(required=False)    

