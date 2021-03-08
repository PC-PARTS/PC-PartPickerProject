from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Build, Case, Cpu_Cooler





def home(request):
	context = {
		'builds': Build.objects.all()
	}
	return render(request, 'builder/home.html', context)



class BuildListView(ListView):
	model = Build
	template_name = 'builder/home.html'
	context_object_name = 'builds'

def login(request):
	return render(request, 'builder/login.html')

def register(request):
	return render(request, 'builder/register.html')

def about(request):
	return render(request, 'builder/about.html')

def builds(request):
	return render(request, 'builder/builds.html')








class CoolerListView(ListView):
	model = Cpu_Cooler
	template_name = 'builder/cpu_coolers.html'
	context_object_name = 'cpu_coolers'

def cpu_coolers(request):
	context = {
		'cpu_coolers': Cpu_Cooler.objects.all()
	}
	return render(request, 'builder/cpu_coolers.html', context)

class CPUListView(ListView):
	model = Cpu
	template_name = 'builder/cpu.html'
	context_object_name = 'cpu'

def cpu(request):
	context = {
		'cpu': Cpu.objects.all()
	}
	return render(request, 'builder/cpu.html', context)

class MoboListView(ListView):
	model = Motherboard
	template_name = 'builder/mobo.html'
	context_object_name = 'mobo'

def mobo(request):
	context = {
		'mobo': Motherboard.objects.all()
	}
	return render(request, 'builder/mobo.html', context)

class Mem1ListView(ListView):
	model = Memory1
	template_name = 'builder/mem1.html'
	context_object_name = 'mem1'

def mem1(request):
	context = {
		'mem1': Memory1.objects.all()
	}
	return render(request, 'builder/mem1.html', context)

class Mem2ListView(ListView):
	model = Memory2
	template_name = 'builder/mem2.html'
	context_object_name = 'mem2'

def mem2(request):
	context = {
		'mem2': Memory2.objects.all()
	}
	return render(request, 'builder/mem2.html', context)

class Storage1ListView(ListView):
	model = Storage1
	template_name = 'builder/storage1.html'
	context_object_name = 'storage1'

def storage1(request):
	context = {
		'storage1': Storage1.objects.all()
	}
	return render(request, 'builder/storage1.html', context)

class Storage2ListView(ListView):
	model = Storage2
	template_name = 'builder/storage2.html'
	context_object_name = 'storage2'

def storage2(request):
	context = {
		'storage2': Storage2.objects.all()
	}
	return render(request, 'builder/storage2.html', context)

class Storage3ListView(ListView):
	model = Storage3
	template_name = 'builder/storage3.html'
	context_object_name = 'storage3'

def storage3(request):
	context = {
		'storage3': Storage3.objects.all()
	}
	return render(request, 'builder/storage3.html', context)

class GPUListView(ListView):
	model = Gpu
	template_name = 'builder/gpu.html'
	context_object_name = 'gpu'

def gpu(request):
	context = {
		'gpu': Gpu.objects.all()
	}
	return render(request, 'builder/gpu.html', context)

class CasesListView(ListView):
	model = Case
	template_name = 'builder/cases.html'
	context_object_name = 'case'

def cases(request):
	context = {
		'cases': Case.objects.all()
	}
	return render(request, 'builder/cases.html', context)

class PsuListView(ListView):
	model = Psu
	template_name = 'builder/psu.html'
	context_object_name = 'psu'

def psu(request):
	context = {
		'psu': Psu.objects.all()
	}
	return render(request, 'builder/psu.html', context)

class Monitor1ListView(ListView):
	model = Monitor1
	template_name = 'builder/mon1.html'
	context_object_name = 'mon1'

def mon1(request):
	context = {
		'mon1': Monitor1.objects.all()
	}
	return render(request, 'builder/mon1.html', context)

class Monitor2ListView(ListView):
	model = Monitor2
	template_name = 'builder/mon2.html'
	context_object_name = 'mon2'

def mon2(request):
	context = {
		'mon2': Monitor2.objects.all()
	}
	return render(request, 'builder/mon2.html', context)

class Monitor3ListView(ListView):
	model = Monitor3
	template_name = 'builder/mon3.html'
	context_object_name = 'mon3'

def mon3(request):
	context = {
		'mon3': Monitor3.objects.all()
	}
	return render(request, 'builder/mon3.html', context)