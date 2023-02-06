from django.http import HttpResponse
from django.shortcuts import render

def intro(request):
    return HttpResponse('Hello, Robert')


def cars(request):
    context = {
        'all_cars':[
            {
                'name_of_brand': 'Dacia',
                'model': '1310',
                'color': 'Blue'
            },
            {
                'name_of_brand': 'Volvo',
                'model': 'v60',
                'color': 'Black'
            },
            {
                'name_of_brand': 'Opel',
                'model': 'Astra',
                'color': 'Red'
            }
        ]
    }

    return render(request, 'intro/list_of_cars.html', context)


def movies(request):
    context = {
        'movies':[
            {
                'name_of_movie': 'James Bond',
                'year_of_appearance': 1965
            },
            {
                'name_of_movie': 'Titanic',
                'year_of_appearance': 1997
            },
            {
                'name_of_movie': 'Gladiator',
                'year_of_appearance': 2000
            }
        ]
    }

    return render(request, 'intro/list_of_movies.html', context)