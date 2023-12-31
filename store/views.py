from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category, Product


def store(request):
    all_products = Product.objects.all()
    context = {'my_products': all_products}

    return render(request, 'store/store.html', context=context)


def categories(request):
    all_categories = Category.objects.all()

    return {'all_categories': all_categories}


def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}

    return render(request, 'store/product-info.html', context)
