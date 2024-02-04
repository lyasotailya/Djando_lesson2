import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import os
# Create your views here.


# def workdir(request):
#     return HttpResponse('<br/>'.join(os.listdir('.')))


def index(request):
    return HttpResponse("<br/>".join([
        # "<a href='/'>Главная страница </a",
        # f"<br/><a href='{reverse('time')}'>Время </a",
        # f"<br/><a href='{reverse('workdir')}'>Рабочий директорий </a",
        # f"<br/><a href='{reverse('hello')}'>hello </a",
        # f"<br/><a href='{reverse('html')}'>html </a",
        # f"<br/><a href='{reverse('pagi')}'>pagi </a",
        f"<a href='{reverse('omlet')}'>Омлет </a",
        f"<br/><a href='{reverse('pasta')}'>Паста </a",
        f"<br/><a href='{reverse('buter')}'>Бутерброд </a",
    ]))


DATA = {
    'omlet': {
        'eggs': 2,
        'milk': 0.1,
        'salt': 0.5,
    },
    'pasta': {
        'spaghetti': 150,
        'parmesan': 50,
        'butter': 20
    },
    'buter': {
        'bread': 1,
        'sausage': 1,
        'cheese': 1,
        'tomato': 1
    }
}


def omlet(request):
    servings = int(request.GET.get('servings', 1))
    context = DATA.get('omlet')
    context.update({'servings': servings})
    return render(request, 'omlet.html', context)


def pasta(request):
    servings = int(request.GET.get('servings', 1))
    context = DATA.get('pasta')
    context.update({'servings': servings})
    return render(request, 'pasta.html', context)


def buter(request):
    servings = int(request.GET.get('servings', 1))
    context = DATA.get('buter')
    context.update({'servings': servings})
    return render(request, 'buter.html', context)


# def hello(request):
#     name = request.GET.get('name')
#     age = int(request.GET.get('age', 20))
#     return HttpResponse(f'hello, {name}, {age}')


# def html(request):
#     context = {
#         'test': 5,
#         'data': [1, 3, 6],
#         'val': 'hello'
#     }
#     return render(request, 'demo.html', context)


# CONTENT = [str(i) for i in range(10000)]
#
#
# def pagi(request):
#     page_number = int(request.GET.get('page', 1))
#     paginator = Paginator(CONTENT, 10)
#     page = paginator.get_page(page_number)
#     context = {
#         'page': page
#     }
#     return render(request, 'pagi.html', context)



