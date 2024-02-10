from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import os
# Create your views here.
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def dish_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    dish_data = DATA.get(dish)
    dct = {}
    context = {
        'recipe': dct
    }
    for key, value in dish_data.items():
        value1 = value * servings
        context.get('recipe').update({key: value1})
    return render(request, 'page.html', context)

