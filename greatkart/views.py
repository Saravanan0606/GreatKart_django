from django.http import HttpResponse
from django.shortcuts import render

from store.models import Product, ReviewAndRating


def home(request):
    products = Product.objects.filter(is_available=True).order_by('created_date')
    
    # Get the reviews
    for product in products:
        reviews = ReviewAndRating.objects.filter(product_id=product.id, status=True)
    
    context = {
        'products': products,
        'reviews': reviews,
    }

    return render(request, 'index.html', context) 