from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from . import forms

def welcome(request):
	return render(request, 'welcome.html')

def contact(request):
	form = forms.ContactForm()

	# buat handle form
	if request.method == 'POST':
		form = forms.ContactForm(request.POST)
		if form.is_valid():

			send_mail(
					'dari kontak website',      # subject
					request.POST['subject'],    # message/pesan
					request.POST['email'],      # email pengirim
					['tomsun@entry.co'],        # email yang dituju
					fail_silently=False,        
				)

			# messages.add_message(request, messages.WARNING, 'text pesan') # kita bisa menggunakan flash message seperti ini
			messages.success(request, 'Berhasil Kirim Email')
			return HttpResponseRedirect(reverse('contact'))

	return render(request, 'contact.html', {'form':form})