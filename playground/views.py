from itertools import product

from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Order, OrderItem, Collection
from tags.models import TaggedItem


def say_hello(request) :
    collection = Collection(title='a')
    collection.name = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()
    collection.id

    

    return render(request, 'hello.html', {'name': 'Edith', 'tags': list(queryset)})