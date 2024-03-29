from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from accounts.forms import SignUpForm

def signup(request):
	if request.method == 'POST':
		
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user_data = user.username
			auth_login(request,user)
			return redirect('requesting',user_data=user_data)
	else:
		form = SignUpForm()
		
	return render(request,'signup.html',{'form':form})

# This module is for creating the signup and it redirects to the page 
#where we accept the company registeration number.