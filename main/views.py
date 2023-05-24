from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.http import HttpResponse

def index(request):
    return render(request, 'main/auto.html')
def register(request):
	if request.method == 'POST':
    	form = UserRegisterForm(request.POST)
    	if form.is_valid():
        	form.save()
        	username = form.cleaned_data.get('username')
        	messages.success(request, f'Создан аккаунт {username}!')
        	return redirect('auth')
	else:
    	form = UserRegisterForm()
	return render(request, 'main/templates/main/reg.html', {'form': form})