from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


def register(request):

	errmsg = ''
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		address = request.POST.get('POST')

		if (form.is_valid() and request.POST.get('address') != ''):
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			

		else:
			if request.POST.get('address') == '':
				errmsg = "must enter an address"
			else:
				errmsg = ''

	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form, 'err' : errmsg})
