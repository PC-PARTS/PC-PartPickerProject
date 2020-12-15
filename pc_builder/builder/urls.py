from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'builder-home'),
    path('login/', views.login, name = 'builder-login'),
    path('register/', views.register, name = 'builder-register'),
]
