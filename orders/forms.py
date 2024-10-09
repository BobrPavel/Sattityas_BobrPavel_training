import re
from django import forms

class CreateOrderForms(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    delivery_address = forms.CharField()
    index_cod = forms.CharField()
    phone_number = forms.CharField()
    email = forms.CharField()
    additional_inforation = forms.CharField(required=False)  




    #валидаторы  
    def clean_phone_number(self):
        data = self.cleanned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")
    
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data