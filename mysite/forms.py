from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, max_length=100, required=True)
    contactNumber = forms.CharField(widget=forms.TextInput,max_length=15, required=True)
    email = forms.EmailField(widget=forms.TextInput,required=True)
    subject = forms.CharField(widget=forms.TextInput,max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)