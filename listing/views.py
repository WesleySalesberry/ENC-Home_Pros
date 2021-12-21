from django.db.models import query_utils
from django.shortcuts import render, get_object_or_404
from .models import Listing, ListingPhoto
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, state_choices, bedroom_choices


def index(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    context = {
        'listings': paged_listing,
    }
    return render(request, 'listing/listings.html', context)


def listing(request, listing_id):
    
    listing = get_object_or_404(Listing, pk=listing_id)
    photos = ListingPhoto.objects.filter(listing=listing)
    
    context = {
        'listing': listing,
        'photos': photos
    }
    return render(request, 'listing/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    print(request)

    """Keywords"""
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            """https://docs.djangoproject.com/en/3.1/ref/models/querysets/#icontains"""
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    """City"""
    if 'keywords' in request.GET:
        city = request.GET['city']
        if city:
            """https://docs.djangoproject.com/en/3.1/ref/models/querysets/#iexact"""
            queryset_list = queryset_list.filter(city__iexact=city)

    """state"""
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    """Bedrooms"""
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            """https://docs.djangoproject.com/en/3.1/ref/models/querysets/#lte"""
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    """Price"""
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listing/search.html', context)