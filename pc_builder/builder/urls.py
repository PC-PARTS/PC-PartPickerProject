from django.urls import path
from .views import BuildListView
from . import views
urlpatterns = [
    path('', BuildListView.as_view(), name = 'builder-home'),
    path('builds/', views.builds, name = 'builder-builds'),
    path('about/', views.about, name = 'builder-about'),

    path('parts/', views.parts, name = 'builder-parts'),

    path('cases/', views.cases, name = 'builder-cases'),
    path('cpu_coolers/', views.cpu_coolers, name = 'builder-cpu_coolers'),
    



]