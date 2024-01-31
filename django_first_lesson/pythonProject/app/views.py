import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import os
# Create your views here.


def time(request):
    return HttpResponse(f'time = {datetime.datetime.now().time()}')


def workdir(request):
    return HttpResponse('<br/>'.join(os.listdir('.')))


def index(request):
    return HttpResponse("<br/>".join([
        "<a href='/'>Главная страница </a",
        f"<br/><a href='{reverse('time')}'>Время </a",
        f"<br/><a href='{reverse('workdir')}'>Рабочий директорий </a"
    ]))

