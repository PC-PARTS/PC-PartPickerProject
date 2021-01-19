from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'builder-home'),
    path('login/', views.login, name = 'builder-login'),
    path('builds/', views.builds, name = 'builder-builds'),
    path('about/', views.about, name = 'builder-about'),
]