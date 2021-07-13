from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.games, name='games'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),

]