from django import forms

class RegistrationForm(forms.Form):
	tag_name=forms.CharField(max_length=25)
	