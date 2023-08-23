from django import forms

class ContactForm(forms.Form):
    f_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(required=True, widget=forms.Textarea)