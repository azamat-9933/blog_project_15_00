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
    path('post/detail/<int:id>/', post_detail_view, name='post_detail_url'),
    path('add/post/', add_post_view, name='add_post_url'),
    path('save/post/', save_post_view, name='save_post_url'),
]