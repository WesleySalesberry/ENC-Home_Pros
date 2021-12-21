from django.shortcuts import render
from listing.models import Listing
from realtor.models import Realtor
from listing.choices import price_choices, state_choices, bedroom_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
    }

    return render(request, 'landing/index.html', context)


def about(request):
    realtor = Realtor.objects.order_by('-hire_date')
    mvp_realtor = Realtor.objects.filter(is_mvp=True)
    context = {
        'realtor': realtor,
        'mvp_realtor': mvp_realtor
    }

    return render(request, 'landing/about.html', context)
