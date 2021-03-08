from django.urls import path
from .views import BuildListView
from . import views
urlpatterns = [
    path('', BuildListView.as_view(), name = 'builder-home'),
    path('builds/', views.builds, name = 'builder-builds'),
    path('about/', views.about, name = 'builder-about'),    
    path('cpu_coolers/', views.cpu_coolers, name = 'builder-cpu_coolers'),
    path('cpu/', views.cpu, name = 'builder-cpu'),
    path('mobo/', views.mobo, name = 'builder-mobo'),
    path('mem1/', views.mem1, name = 'builder-mem1'),
    path('mem2/', views.mem2, name = 'builder-mem2'),
    path('storage1/', views.storage1, name = 'builder-storage1'),
    path('storage2/', views.storage2, name = 'builder-storage2'),
    path('storage3/', views.storage3, name = 'builder-storage3'),
    path('gpu/', views.gpu, name = 'builder-gpu'),
    path('cases/', views.cases, name = 'builder-cases'),
    path('psu/', views.psu, name = 'builder-psu'),
    path('mon1/', views.mon1, name = 'builder-mon1'),
    path('mon2/', views.mon2, name = 'builder-mon2'),
    path('mon3/', views.mon3, name = 'builder-mon3'),
]