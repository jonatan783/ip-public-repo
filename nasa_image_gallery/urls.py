from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),

    path('exit/', views.exit, name='exit'),
]