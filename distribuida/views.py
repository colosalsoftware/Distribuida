from django.http import HttpResponse
from django.shortcuts import render
from miapp.models import *
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
def home(request):
    return render(request,'miapp/index.html')
