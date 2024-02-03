from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import Subs

def home(request):
	return render(request,'pages/home.html')

def movies(request):
	return render(request,'pages/movies.html')

def about(request):
	return render(request,'pages/about.html')

def navbar(request):
	return render(request,'pages/navbar.html')

def food(request):
	return render(request,'pages/food.html')

def login(request):
	return render(request,'pages/login.html')

def contact(request):
	return render(request,'pages/contact.html')

def spiderman(request):
	return render(request,'pages/spiderman.html')

def mermaid(request):
	return render(request,'pages/mermaid.html')

def indiana(request):
	return render(request,'pages/indiana.html')

def transformers(request):
	return render(request,'pages/transformers.html')

def cart(request):
	return render(request,'pages/cart.html')

def profile(request, pk):
	subs = Subscription.objects.get(id=pk)
	context = {
		'subs':subs,
	}

	return render(request,'pages/profile.html', context)
	
def main(request):
	subs = Subscription.objects.all()
	total_subs = subs.count()

	context = {
		'subs':subs,
		'total_subs':total_subs
	}
	return render(request,'pages/main.html' , {'subs' :subs})

def subscription(request):
	form = Subs()
	if request.method == 'POST':
		form = Subs(request.POST)
		if form.is_valid():
			form.save()
			return redirect('main')

	context = {
		'form':form
	}
	return render(request,'pages/subscription.html', context)

def update(request, pk):
	subs = Subscription.objects.get(id=pk)
	form = Subs(instance=subs)

	if request.method == 'POST':
		form = Subs(request.POST, instance=subs)
		if form.is_valid():
			form.save()
			return redirect('main')

	context = {'form':form}
	return render(request, 'pages/subscription.html', context)

def delete(request, pk):
	subs = Subscription.objects.get(id=pk)
	if request.method == 'POST':
		subs.delete()
		return redirect('main')

	context = {
		'subs':subs
	}
	return render(request,'pages/delete.html', context)