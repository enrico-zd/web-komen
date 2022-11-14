from django import forms
from django.core import validators

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	subject = forms.CharField(widget=forms.Textarea)
	# # untuk clean_method
	# honeypot = forms.CharField(widget=forms.Textarea, required=False) 
	honeypot = forms.CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

	# def clean_honeypot(self):
	# 	honeypot = self.cleaned_data['honeypot']
	# 	if len(honeypot):    # cek apa ada panjang di honeypot
	# 		raise forms.ValidationError('Ngga boleh diisi dong')
	# 	# jika tidak ada kita return honeypot
	# 	return honeypot