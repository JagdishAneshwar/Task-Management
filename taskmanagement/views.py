from django.shortcuts import render,redirect, HttpResponseRedirect
from .models import member, task
from django.contrib.auth.models import User, auth
from .forms import users,tasks
from django.core.mail import send_mail
from django.contrib import messages
import asynchat
import asyncore
# Create your views here

def about(request):
	return render(request, 'about.html', {})

def signup(request):
	if request.method == 'POST':
		username = request.POST['name']
		password1 = request.POST['pwd']
		password2 = request.POST['pwd2']
		email = request.POST['email']
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, "Username is Already Taken!!")
				return redirect('signup.html')
			else:
				user = User.objects.create_user(username=username, password=password1, email=email)
				user.save()
				user = auth.authenticate(username=username, password=password1)
				auth.login(request, user)
				return redirect('all_task.html')

		else:
			messages.info(request, "Password didn't match!!")
			return redirect('signup.html')

	else:
		return render(request, 'signup.html', {})

def login(request):
	if request.method == 'POST':
		username = request.POST['user']
		password = request.POST['pwd']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('all_member.html')
		else:
			messages.info(request, "Password or Username Is Wrong!!")
			return redirect('login.html')
	else:
		return render(request, 'login.html', {})

def logout(request):
	auth.logout(request)
	return redirect('about.html')

def add_member(request):
	if request.method == 'POST':
		form = users(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['name']
			role = form.cleaned_data['role']
			img = request.FILES['upload']
			request.user.member_set.create(name=name, role=role, upload=img)
			return redirect('all_member.html')
		else:
			messages.info(request, "fields can't be Empty")
			return redirect('add_member.html')
	else:
		form = users()
		return render(request, 'add_member.html', {'form':form})

def all_member(request):
	lis = member.objects.filter(member_id=request.user)
	return render(request, 'all_member.html', {'lis' : lis})

def add_task(request):
	if request.method == 'POST':
		form = tasks(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			desc = form.cleaned_data['desc']
			due = form.cleaned_data['due']
			request.user.task_set.create(name=name, desc=desc, due=due)
			return redirect('all_task.html')
	else:
		return render(request, 'add_task.html', {})

def all_task(request):
	lis = task.objects.filter(task_id=request.user)
	return render(request, 'all_task.html', {'lis' : lis})

def ind_dtl(request):
	return render(request, 'ind_dtl.html', {})

def delete_task(request, item_id):
	if request.method == 'POST':
		dl = task.objects.get(pk=item_id)
		dl.delete()
		return redirect('/all_task.html')

def delete_member(request, item_id):
	if request.method == 'POST':
		dl = member.objects.get(pk=item_id)
		dl.delete()
		return redirect('/all_member.html')













