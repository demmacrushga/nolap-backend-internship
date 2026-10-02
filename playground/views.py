from itertools import product

from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist


def say_hello(request) :

    exists = Product.objects.filter(pk=0).exists()

    return render(request, 'hello.html', {'name': 'Edith', 'exists': exists})