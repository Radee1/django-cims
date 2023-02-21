from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# flash messages
from django.contrib import messages
# user database
from django.contrib.auth.models import User
from .models import Diagnosis, Appointment, Medicine, Patient, Team
# authenticate
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.


def index(request):
    return render(request, 'cim_users/user_login.html')


def handler404(request, exception):
    return render(request, 'cim_users/handler404.html', status=404)


def home(request):
    patients = Patient.objects.all().count()
    diagnosis = Diagnosis.objects.all().count()
    medicine = Medicine.objects.all().count()
    appointments = Appointment.objects.all().count()
    return render(request, 'cim_users/index.html', {'patients': patients, 'diagnosis': diagnosis, 'medicine': medicine, 'appointments': appointments})

# loging


def login(request):
    return render(request, 'cim_users/user_login.html')


def login_user(request):
    user_name = request.POST['username']
    user_password = request.POST['password']
    if User.objects.filter(username=user_name).first():
        print("This username exists")
        user = authenticate(request, username=user_name, password=user_password)
        if user is not None:
            Welcome = user_name+' Logged in Successfully'
            # login
            auth_login(request, user)
            messages.success(request, Welcome)
            # redirect
            return redirect('cim_users:home')
        else:
            # No authenticated the credentials
            messages.error(request, 'Wrong Username or Password.')
            return render(request, 'cim_users/user_login.html')
    else:
        messages.success(request, 'Credentials do not exist.')
        return render(request, 'cim_users/user_login.html')


@login_required
def logout_user(request):
    auth_logout(request)
    messages.success(request, 'You have logged out. Bye!')
    return redirect('cim_users:login')


def create_user(request):
    user_name = request.POST['username']
    user_password = request.POST['password']
    user_email = request.POST['email']
    if User.objects.filter(username=user_name).first():
        messages.info(request, 'Account already exists')
        return render(request, 'cim_users/user_create.html')
    else:
        User.objects.create_user(username=user_name, password=user_password, email=user_email)
        messages.success(request, 'Account created.')
        # Redirect to a success page.
        return render(request, 'cim_users/user_login.html')


def create_user_page(request):
    # Redirect to a success page.
    return render(request, 'cim_users/user_create.html')


def services(request):
    return render(request, 'cim_users/services.html')


def team(request):
    t_data = Team.objects.all()
    t_number = t_data.count()
    return render(request, 'cim_users/team.html', {'t_data': t_data, 't_number': t_number})


def add_member(request):
    if request.POST:
        full_name = request.POST['full_name']
        position = request.POST['position']
        department = request.POST['department']
        if Team.objects.filter(full_name=full_name).first():
            messages.info(request, 'Team member already exists')
            return redirect('cim_users:team')
        else:
            messages.success(request, 'Team member successfully added.')
            member = Team.objects.create(full_name=full_name, position=position, department=department)
            return redirect('cim_users:team')
    else:
        return render('cim_users:team')


def delete_member(request):
    member_id = request.POST['member_id']
    member = Team.objects.get(id=member_id)
    member.delete()
    messages.success(request, 'Member deleted.')
    return redirect('cim_users:team')


def update_member(request):
    full_name = request.POST['full_name']
    member_id = request.POST['Team_ID']
    position = request.POST['position']
    department = request.POST['department']
    member = Team.objects.get(id=member_id)
    member.full_name = full_name
    member.position = position
    member.department = department
    member.save()
    messages.success(request, 'Member details updated.')
    return redirect('cim_users:team')


def appointments(request):
    a_data = Appointment.objects.all()
    a_number = a_data.count()
    # doctors data
    d_data = Team.objects.all().filter(position='Doctor')
    # Redirect to a success page.
    return render(request, 'cim_users/appointments.html', {'a_data': a_data, 'd_data': d_data, 'a_number': a_number})


def make_appointment(request):
    if request.POST:
        user_name = request.POST['Patient_Name']
        doctor = request.POST['doctor']
        time = request.POST['time']
        if Appointment.objects.filter(patient_name=user_name).first():
            messages.info(request, 'Patient appointment already exists')
            return redirect('cim_users:appointments')
        else:
            Appointment.objects.create(patient_name=user_name, doctor=doctor, time=time)
            messages.success(request, 'Appointment created.')
            # Redirect to a success page.
            return redirect('cim_users:appointments')
    else:
        return render('cim_users:appointments')


def delete_appointment(request):
    a_name = request.POST['Patient_Name']
    appointment = Appointment.objects.get(patient_name=a_name)
    appointment.delete()
    messages.success(request, 'Appointment deleted.')
    return redirect('cim_users:appointments')


def update_appointment(request):
    user_name = request.POST['Patient_Name']
    a_id = request.POST['Appointment_ID']
    doctor = request.POST['doctor']
    time = request.POST['time']
    appointment = Appointment.objects.get(id=a_id)
    appointment.patient_name = user_name
    appointment.doctor = doctor
    appointment.time = time
    appointment.save()
    messages.success(request, 'Appointment updated.')
    return redirect('cim_users:appointments')


def diagnosis(request):
    d_data = Diagnosis.objects.all()
    d_number = d_data.count()
    return render(request, 'cim_users/diagnosis.html', {'d_data': d_data, 'd_number': d_number})


def add_diagnosis(request):
    if request.POST:
        name = request.POST['Patient_Name']
        test_name = request.POST['test_name']
        diagnosis = request.POST['diagnosis']

        if Diagnosis.objects.filter(patient_name=name).first():
            messages.info(request, 'Patient already diagnized')
            return redirect('cim_users:diagnosis')
        else:
            Diagnosis.objects.create(patient_name=name, test_name=test_name, diagnosis=diagnosis)
            messages.success(request, 'Diagnosis created.')
            # Redirect to a success page.
            return redirect('cim_users:diagnosis')
    else:
        return render('cim_users:diagnosis')


def delete_diagnosis(request):
    d_name = request.POST['Patient_Name']
    diagnosis = Diagnosis.objects.get(patient_name=d_name)
    diagnosis.delete()
    messages.success(request, 'Diagnosis deleted.')
    return redirect('cim_users:diagnosis')


def update_diagnosis(request):
    patient_name = request.POST['Patient_Name']
    d_id = request.POST['Diagnosis_ID']
    test_name = request.POST['test_name']
    diagnosis_name = request.POST['diagnosis']
    diagnosis = Diagnosis.objects.get(id=d_id)
    diagnosis.patient_name = patient_name
    diagnosis.diagnosis = diagnosis_name
    diagnosis.test_name = test_name
    diagnosis.save()
    messages.success(request, 'Diagnosis updated.')
    return redirect('cim_users:diagnosis')


def treatment(request):
    med_data = Medicine.objects.all()
    number = med_data.count()
    return render(request, 'cim_users/pharmacy.html', {'number': number, 'med_data': med_data})


def add_treatment(request):
    if request.POST:
        drug_name = request.POST['medicine']
        prescribed_to = request.POST['Patient_Name']
        stock = request.POST['stock']
        if Medicine.objects.filter(prescribed_to=prescribed_to).first():
            messages.info(request, 'Prescription already exists')
            return redirect('cim_users:treatment')
        else:
            messages.success(request, 'Prescription created.')
            prescribed = Medicine.objects.create(prescribed_to=prescribed_to, drug_name=drug_name, stock=stock)
            drug_data = Medicine.objects.all()
            # Redirect to a success page.
            return redirect('cim_users:treatment')
    else:
        return render('cim_users:treatment')


def delete_treatment(request):
    prescribed_to = request.POST['Patient_Name']
    treatment = Medicine.objects.get(prescribed_to=prescribed_to)
    treatment.delete()
    messages.success(request, 'Prescription deleted.')
    return redirect('cim_users:treatment')


def update_treatment(request):
    prescribed_to = request.POST['Patient_Name']
    treatment_id = request.POST['Treatment_ID']
    drug_name = request.POST['medicine']
    stock = request.POST['stock']
    treatment = Medicine.objects.get(id=treatment_id)
    treatment.prescribed_to = prescribed_to
    treatment.drug_name = drug_name
    treatment.stock = stock
    treatment.save()
    messages.success(request, 'Prescription updated.')
    return redirect('cim_users:treatment')


def add_patient(request):
    if request.POST:
        user_name = request.POST['Patient_Name']
        ailment = request.POST['ailment']
        if Patient.objects.filter(full_name=user_name).first():
            messages.info(request, 'Patient record already exists')
            return redirect('cim_users:patients')
        else:
            patient = Patient.objects.create(full_name=user_name, symptoms=ailment)
            messages.success(request, 'Patient record created.')
            # Redirect to a success page.
            return redirect('cim_users:patients')
    else:
        return render(request, 'cim_users/patients.html')


def patients(request):
    p_data = Patient.objects.all()
    p_number = p_data.count()
    # Redirect to a success page.
    return render(request, 'cim_users/patients.html', {'p_data': p_data, 'p_number': p_number})


def delete_patient(request):
    p_name = request.POST['Patient_Name']
    patient = Patient.objects.get(full_name=p_name)
    patient.delete()
    messages.success(request, 'Patient record deleted.')
    return redirect('cim_users:patients')


def update_patient(request):
    user_name = request.POST['Patient_Name']
    p_id = request.POST['Patient_ID']
    ailment = request.POST['ailment']
    user = Patient.objects.get(id=p_id)
    user.full_name = user_name
    user.diagnosis = diagnosis
    user.symptoms = ailment
    user.save()
    messages.success(request, 'Patient record updated.')
    return redirect('cim_users:patients')
