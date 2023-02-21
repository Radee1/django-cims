from django.shortcuts import render

def index(request):
    return render(request,'cim_users/about.html')
