from django.db import models
from django.contrib.auth.models import User

class Build(models.Model):
	
	cpu = models.CharField(max_length=100)
	cpu_cooler = models.CharField(max_length=100)
	motherboard = models.CharField(max_length=100)
	memory1 = models.CharField(max_length=100)
	memory2 = models.CharField(max_length=100,blank=True,null=True)
	storage1 = models.CharField(max_length=100)
	storage2 = models.CharField(max_length=100,blank=True,null=True)
	storage3 = models.CharField(max_length=100,blank=True,null=True)
	gpu = models.CharField(max_length=100)
	case = models.CharField(max_length=100)
	psu = models.CharField(max_length=100)
	os = models.CharField(max_length=100,blank=True,null=True)
	monitor1 = models.CharField(max_length=100,blank=True,null=True)
	monitor2 = models.CharField(max_length=100,blank=True,null=True)
	monitor3 = models.CharField(max_length=100,blank=True,null=True)
# Create your models here.

class Cpu(models.Model):

	cpu_name = models.CharField(max_length=100)
	core_count = models.CharField(max_length=100)
	core_clock = models.CharField(max_length=100)
	boost_clock = models.CharField(max_length=100)
	tdp = models.CharField(max_length=100)
	intigrated_graphics = models.CharField(max_length=100)
	smt = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)

class Cpu_Cooler(models.Model):

	cpu_cooler_name = models.CharField(max_length=100)
	fan_rpm = models.CharField(max_length=100)
	noise_level = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	radiator_size = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)

class Motherboard(models.Model):

	m_board_name = models.CharField(max_length=100)
	socket_cpu = models.CharField(max_length=100)
	form_factor = models.CharField(max_length=100)
	memory_max = models.CharField(max_length=100)
	memory_slots = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)

class Memory1(models.Model):

	mem_name = models.CharField(max_length=100)
	speed = models.CharField(max_length=100)
	modules = models.CharField(max_length=100)
	price_gb = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	f_word_latency = models.CharField(max_length=100)
	cas_latency = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)

class Memory2(models.Model):

	mem_name = models.CharField(max_length=100)
	speed = models.CharField(max_length=100)
	modules = models.CharField(max_length=100)
	price_gb = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	f_word_latency = models.CharField(max_length=100)
	cas_latency = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)

class Storage1(models.Model):

	storyage_name = models.CharField(max_length=100)
	capacity = models.CharField(max_length=100)
	price_gb = models.CharField(max_length=100)
	storage_type = models.CharField(max_length=100)
	cache = models.CharField(max_length=100)
	form_factor = models.CharField(max_length=100)
	interface = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	
class Storage2(models.Model):

	storyage_name = models.CharField(max_length=100)
	capacity = models.CharField(max_length=100)
	price_gb = models.CharField(max_length=100)
	storage_type = models.CharField(max_length=100)
	cache = models.CharField(max_length=100)
	form_factor = models.CharField(max_length=100)
	interface = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)

class Storage3(models.Model):

	storyage_name = models.CharField(max_length=100)
	capacity = models.CharField(max_length=100)
	price_gb = models.CharField(max_length=100)
	storage_type = models.CharField(max_length=100)
	cache = models.CharField(max_length=100)
	form_factor = models.CharField(max_length=100)
	interface = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)

class Gpu(models.Model):

	gpu_name = models.CharField(max_length=100)
	chipset = models.CharField(max_length=100)
	memory = models.CharField(max_length=100)
	core_clock = models.CharField(max_length=100)
	boost_clock = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	length = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	
class Case(models.Model):

	case_name = models.CharField(max_length=100)
	case_type = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	power_supply = models.CharField(max_length=100)
	side_pannel_window = models.CharField(max_length=100)
	external_bays = models.CharField(max_length=100)
	internal_bays = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	
class Psu(models.Model):

	power_name = models.CharField(max_length=100)
	f_factor = models.CharField(max_length=100)
	efficency_rating = models.CharField(max_length=100)
	wattage = models.CharField(max_length=100)
	modular = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	
class Os(models.Model):

	os_name = models.CharField(max_length=100)
	BD = models.CharField(max_length=100)
	DVD = models.CharField(max_length=100)
	CD = models.CharField(max_length=100)
	BD_write = models.CharField(max_length=100)
	DVD_write = models.CharField(max_length=100)
	CD_write = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	
class Monitor1(models.Model):

	monitor_name = models.CharField(max_length=100)
	screen_size = models.CharField(max_length=100)
	resolution = models.CharField(max_length=100)
	refresh_rate = models.CharField(max_length=100)
	response_time = models.CharField(max_length=100)
	panel_type = models.CharField(max_length=100)
	aspect_ratio = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	
class Monitor2(models.Model):

	monitor_name = models.CharField(max_length=100)
	screen_size = models.CharField(max_length=100)
	resolution = models.CharField(max_length=100)
	refresh_rate = models.CharField(max_length=100)
	response_time = models.CharField(max_length=100)
	panel_type = models.CharField(max_length=100)
	aspect_ratio = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	
class Monitor3(models.Model):

	monitor_name = models.CharField(max_length=100)
	screen_size = models.CharField(max_length=100)
	resolution = models.CharField(max_length=100)
	refresh_rate = models.CharField(max_length=100)
	response_time = models.CharField(max_length=100)
	panel_type = models.CharField(max_length=100)
	aspect_ratio = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	
