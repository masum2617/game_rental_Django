from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def games(request):
    game_listings = Listing.objects.all()
    paginator = Paginator(game_listings, 3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'game_listings' : page_listings
    }
    return render(request, 'games/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'game_listing' : listing
    }
    return render(request, 'games/listing.html', context)

def search(request):
    return render(request, 'games/search.html')