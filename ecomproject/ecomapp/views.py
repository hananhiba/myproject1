from django.shortcuts import render, get_object_or_404

from ecomapp.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.


def AllProductCategory(request, category_slug=None):
    category_page = None
    products_list = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products_list = Product.objects.all().filter(category=category_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list, 6)
    try:
        page1 = int(request.GET.get('page', '1'))
    except:
        page1 = 1
    try:
        products = paginator.page(page1)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': category_page, 'products': products})


def proDetail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, "product.html", {'product': product})
