from django.contrib import admin
from .models import Listing, ListingPhoto


class ListingPhotoAdmin(admin.StackedInline):
    model = ListingPhoto


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):

    inlines = [ListingPhotoAdmin]

    class Meta:
        model = Listing

    list_display = ('id', 'title', 'is_published', 'list_date',
                    'city', 'state', "zipcode", 'price', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode', 'price')
    list_per_page = 25

