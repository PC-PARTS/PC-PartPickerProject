from django.contrib import admin
from .models import Build, Cpu, Cpu_Cooler, Motherboard, Memory1, Memory2, Storage1, Storage2, Storage3, Gpu, Case, Psu, Monitor1, Monitor2, Monitor3

admin.site.register(Build)
# Register your models here.
admin.site.register(Cpu)
admin.site.register(Cpu_Cooler)
admin.site.register(Motherboard)
admin.site.register(Memory1)
admin.site.register(Memory2)
admin.site.register(Storage1)
admin.site.register(Storage2)
admin.site.register(Storage3)
admin.site.register(Gpu)
admin.site.register(Case)
admin.site.register(Psu)
admin.site.register(Monitor1)
admin.site.register(Monitor2)
admin.site.register(Monitor3)
