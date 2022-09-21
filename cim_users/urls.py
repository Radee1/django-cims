from django.urls import path
from . import views

# Users urls defined here
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('services', views.services, name='services'),
    path('team', views.team, name='team'),
]