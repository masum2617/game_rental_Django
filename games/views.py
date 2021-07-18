from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .genre import genreCategory

def games(request):
    game_listings = Listing.objects.all()
    paginator = Paginator(game_listings, 3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'game_listings' : page_listings,
        'genreCategory': genreCategory,
    }
    return render(request, 'games/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'game_listing' : listing
    }
    return render(request, 'games/listing.html', context)

def search(request):
    query_gameList = Listing.objects.all()

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_gameList = query_gameList.filter(game_title__icontains=keywords)
    
    if 'genre' in request.GET:
        genre = request.GET['genre']
        if genre:
            query_gameList = query_gameList.filter(genre__iexact=genre)

    context = {
        'game_listings' : query_gameList,
        'genreCategory': genreCategory,
        
    }
    return render(request, 'games/search.html', context)