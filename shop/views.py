from django.core import paginator
from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    products = models.Product.objects.filter(status=True)[:6]
    return render(request, 'shop/index.html', locals())

def product(request):
    category = models.Category.objects.filter(status=True).first()
    products = models.Product.objects.filter(
        category__name=category.name,
        status=True
        )
    paginator = Paginator(products, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/shop.html', {'page_obj':page_obj})

def product_detail(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    return render(request, 'shop/product-details.html', locals())

def product_category(request, name):
    products = models.Product.objects.filter(category__name=name, status=True)
    paginator = Paginator(products, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/product-categories.html', {'page_obj':page_obj})

def news(request):
    start_date = datetime.now() - timedelta(days=7)
    end_date = datetime.now() + timedelta(days=1)
    products = models.Product.objects.filter(
        Q(date_add__gte=start_date) & Q(date_add__lt=end_date)
    )

    paginator = Paginator(products, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 
        'shop/new-products.html', 
        {'page_obj':page_obj}
        )