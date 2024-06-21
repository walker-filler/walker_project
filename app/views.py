from django.shortcuts import render
from app.models import Product


def product_list(request):
    all_products = Product.objects.all()
    return render(request, "app/product_list.html", {"products": all_products})
