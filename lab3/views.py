from django.shortcuts import render, render_to_response


# Create your views here.
from lab3.models import Product, Recall


def home(request):
    data = {}
    user_name = None
    if request.user.is_authenticated():
        user_name = request.user.username
    products = Product.objects.all()
    recalls = Recall.objects.all()
    data['user_name'] = user_name
    data['products'] = products
    data['recalls'] = recalls
    return render_to_response('home.html', data)
