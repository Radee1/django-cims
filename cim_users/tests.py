from django.test import TestCase, Client
from .models import Patient, Medicine, Appointment, Diagnosis
from django.urls import reverse


class PatientIndexViewTests(TestCase):
    def test_patients(self):
        """
        If  Patients view exist.
        """
        response = self.client.get(reverse('cim_users:patients'))
        self.assertEqual(response.status_code, 200)


class PatientTestCase(TestCase):
    def setUp(self):
        Patient.objects.create(
                               full_name="John Doe",
                               symptoms="Fever",
                               diagnosis="Malaria")
        Patient.objects.create(
                               full_name="Jane Din",
                               symptoms="Cough",
                               diagnosis="Cold")

    def test_patient_can_be_created(self):
        """Patients can be created."""
        p1 = Patient.objects.get(full_name="John Doe")
        p2 = Patient.objects.get(full_name="Jane Din")
        self.assertEqual(p1.full_name, 'John Doe')
        self.assertEqual(p2.full_name, 'Jane Din')


class MedicineIndexViewTests(TestCase):
    def test_medicine(self):
        """
        If  Pharmacy/medicine view exist.
        """
        response = self.client.get(reverse('cim_users:treatment'))
        self.assertEqual(response.status_code, 200)


class MedicineTestCase(TestCase):
    def setUp(self):
        Medicine.objects.create(drug_name="Coartem", stock="3 strips")
        Medicine.objects.create(drug_name="Panadol", stock="2 strips")

    def test_medicine_can_be_issued(self):
        """Medicine can be issued."""
        m1 = Medicine.objects.get(drug_name="Coartem")
        m2 = Medicine.objects.get(drug_name="Panadol")
        self.assertEqual(m1.drug_name, 'Coartem')
        self.assertEqual(m2.drug_name, 'Panadol')


class AppointmentIndexViewTests(TestCase):
    def test_appointments(self):
        """
        If  Patients view exist.
        """
        response = self.client.get(reverse('cim_users:appointments'))
        self.assertEqual(response.status_code, 200)


class AppointmentTestCase(TestCase):
    def setUp(self):
        Appointment.objects.create(patient_name="John Doe", doctor="Dr James")
        Appointment.objects.create(patient_name="Jane Din", doctor="Dr Rose")

    def test_appointment_can_be_created(self):
        """Appointments can be created."""
        a1 = Appointment.objects.get(patient_name="John Doe")
        a2 = Appointment.objects.get(patient_name="Jane Din")
        self.assertEqual(a1.patient_name, 'John Doe')
        self.assertEqual(a2.patient_name, 'Jane Din')


class DiagnosisIndexViewTests(TestCase):
    def test_diagnosis(self):
        """
        If  Diagnosis view exists.
        """
        response = self.client.get(reverse('cim_users:diagnosis'))
        self.assertEqual(response.status_code, 200)


class DiagnosisTestCase(TestCase):
    def setUp(self):
        Diagnosis.objects.create(
                                 patient_name="John Doe",
                                 test_name="Malaria Test",
                                 diagnosis="Malaria Positive")
        Diagnosis.objects.create(
                                 patient_name="Jane Din",
                                 test_name="Sputum test",
                                 diagnosis="Covid Positive")

    def test_diagnosis_can_be_created(self):
        """Diagnosis can be created."""

        d1 = Diagnosis.objects.get(patient_name="John Doe")
        d2 = Diagnosis.objects.get(patient_name="Jane Din")
        self.assertEqual(d1.patient_name, 'John Doe')
        self.assertEqual(d2.patient_name, 'Jane Din')
