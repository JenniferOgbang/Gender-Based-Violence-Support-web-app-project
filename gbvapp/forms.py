from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='Enter your email')