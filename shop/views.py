from django.core.paginator import Paginator
from .models import Shop
from django.shortcuts import render

# Create your views here.
def shop(request):
    shop_listings = Shop.objects.all()
    paginator = Paginator(shop_listings, 3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'shop_listings': page_listings,
    }
    return render(request, 'shop/shop.html', context)