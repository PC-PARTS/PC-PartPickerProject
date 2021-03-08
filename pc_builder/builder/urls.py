from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'builder-home'),
    path('builds/', views.builds, name = 'builder-builds'),
    path('about/', views.about, name = 'builder-about'),
    path('parts/', views.parts, name = 'builder-parts'),
]