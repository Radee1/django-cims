from django.urls import path
from . import views

# Users urls defined here
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('create_user_page', views.create_user_page, name='create_user_page'),
    path('create_user', views.create_user, name='create_user'),
    path('services', views.services, name='services'),
    path('team', views.team, name='team'),
    path('appointments', views.appointments, name='appointments'),
    path('make_appointment', views.make_appointment, name='make_appointment'),
    path('update_appointment', views.update_appointment, name='update_appointment'),
    path('delete_appointment', views.delete_appointment, name='delete_appointment'),
    path('diagnosis', views.diagnosis, name='diagnosis'),
    path('add_diagnosis', views.add_diagnosis, name='add_diagnosis'),
    path('update_diagnosis', views.update_diagnosis, name='update_diagnosis'),
    path('delete_diagnosis', views.delete_diagnosis, name='delete_diagnosis'),
    path('treatment', views.treatment, name='treatment'),
    path('add_patient/', views.add_patient, name='add_patient/'),
    path('patients/', views.patients, name='patients/'),
    path('update_patient', views.update_patient, name='update_patient'),
    path('delete_patient', views.delete_patient, name='delete_patient'),
]