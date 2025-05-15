from django.shortcuts import render

def home(request):
    return render(request, 'city_site/index.html')
