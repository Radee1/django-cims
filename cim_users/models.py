from django.db import models

# Create your models here.
class Usaz(models.Model):
    user_ID = models.CharField(max_length=10)
    user_name = models.CharField(max_length=20)
    sign_in_time = models.DateTimeField(auto_now=True)

class Patient(models.Model):
    full_name = models.CharField(max_length=80)
    symptoms = models.CharField(max_length=200)
    diagnosis = models.CharField(max_length=200)
    time_of_visit = models.DateTimeField(auto_now=True)

class Diagnosis(models.Model):
    patient_name = models.CharField(max_length=80)
    test_name = models.CharField(max_length=200)
    diagnosis = models.CharField(max_length=200)
    time_of_visit = models.DateTimeField(auto_now=True)

class Appointment(models.Model):
    patient_name = models.CharField(max_length=80)
    doctor = models.CharField(max_length=200)
    time = models.CharField(max_length=200)

class Medicine(models.Model):
    drug_name = models.CharField(max_length=80)
    stock = models.CharField(max_length=200)
    prescribed_to = models.CharField(max_length=200)