"""Django Cims Models."""
from django.db import models


class Usaz(models.Model):
    """User Model."""

    user_ID = models.CharField(max_length=10)
    user_name = models.CharField(max_length=20)
    sign_in_time = models.DateTimeField(auto_now=True)


class Patient(models.Model):
    """Patient Model."""

    full_name = models.CharField(max_length=80)
    symptoms = models.CharField(max_length=200)
    time_of_visit = models.DateTimeField(auto_now=True)


class Team(models.Model):
    """Team Model."""

    full_name = models.CharField(max_length=80)
    position = models.CharField(max_length=200)
    department = models.CharField(max_length=200)


class Diagnosis(models.Model):
    """Diagnosis Model."""

    patient_name = models.CharField(max_length=80)
    test_name = models.CharField(max_length=200)
    diagnosis = models.CharField(max_length=200)
    time_of_visit = models.DateTimeField(auto_now=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    doctor_id = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)


class Appointment(models.Model):
    """Appointment Model."""

    patient_name = models.CharField(max_length=80)
    doctor = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    doctor_id = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)


class Medicine(models.Model):
    """Medicine Model."""

    drug_name = models.CharField(max_length=80)
    stock = models.CharField(max_length=200)
    prescribed_to = models.CharField(max_length=200)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
