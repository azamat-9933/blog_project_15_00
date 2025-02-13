from django.urls import path

from blog.views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('about_us/', about_us_view, name='about_us_url'),
    path('our_team/', our_team_view, name='our_team_url'),
    path('contacts/', contacts_view, name='contacts_url'),
    path('services/', services_view, name='services_url'),
    path('category/<str:slug>/', category_view, name='category_url'),
    path('results/', search_view, name='search_url'),
]