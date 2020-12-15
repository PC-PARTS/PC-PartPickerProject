from django.shortcuts import render
from django.http import HttpResponse


builds = [
	{
		'title':'build name here',
		'gpu':'RTX 3080',
		'cpu': 'Ryzen 9 3700x',
		'motherboard': 'Asus ROG STRIX B550-F GAMING (WI-FI) ATX AM4 Motherboard'		
	}
]


def home(request):
	context = {
		'builds': builds
	}
	return render(request, 'builder/home.html',context)

def login(request):
	return render(request, 'builder/login.html')

def register(request):
	return render(request, 'builder/register.html')
# Create your views here.
