from datetime import datetime
from django import forms
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf


# Create your views here.
from lab3.models import Product, Recall, City


class RecallForm(forms.Form):
    text = forms.CharField(max_length=200)


def home(request, city_id=1):
    data = {}
    user_name = None
    if request.user.is_authenticated():
        user_name = request.user.username
    products = Product.objects.filter(city=city_id)
    recalls = Recall.objects.all()
    cities = City.objects.all()
    data['user_name'] = user_name
    data['products'] = products
    data['recalls'] = recalls
    data['cities'] = cities
    return render_to_response('home.html', data)


def product(request, product_id):
    data = {}
    data.update(csrf(request))
    user_name = None
    if request.user.is_authenticated():
        user_name = request.user.username
    if request.method == 'POST':
        form = RecallForm(request.POST)
        if form.is_valid():
            new_recall = Recall(
                user_id=request.user,
                product_id=Product.objects.get(id=product_id),
                text=form.cleaned_data['text'])
            new_recall.save()
    product = Product.objects.get(id=product_id)
    cities = City.objects.all()
    recalls = Recall.objects.filter(product_id=product_id)
    data['product'] = product
    data['cities'] = cities
    data['recalls'] = recalls
    data['user_name'] = user_name
    return render_to_response('product.html', data)
