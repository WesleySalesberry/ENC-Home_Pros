from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('landing.urls')),
    path('listings/', include('listing.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
]
