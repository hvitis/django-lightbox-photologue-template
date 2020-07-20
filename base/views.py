from django.shortcuts import render

# Example dynamic data
from datetime import date

# Tailwinds CSS homepage
def homepage(request):
    return render(request, 'base/homepage.html',)

# Bootstrap Homepage
def bootstrap(request):

    this_year = date.today().year

    return render(request, 'bootstrap/bootstrap.html', context={
        'year': this_year,
    })