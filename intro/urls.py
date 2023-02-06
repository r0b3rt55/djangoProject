from django.urls import path

from intro import views

urlpatterns = [
    path('first-page', views.intro, name='first_page'),
    path('list-of-cars/', views.cars, name='list_of_cars'),
    path('list-of-movies/', views.movies, name='list_of_movies')
]