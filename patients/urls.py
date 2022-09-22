from django.urls import path
from . import views

#Patient Urls written here
urlpatterns = [
    path('', views.index, name='index'),
    path('patients', views.index, name='patients'),
    path('appointments', views.appointments, name='appointments'),
    path('diagnosis', views.diagnosis, name='diagnosis'),
    path('treatment', views.treatment, name='treatment'),
]