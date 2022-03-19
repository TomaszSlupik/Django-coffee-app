from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Coffee


def all_coffee (request):
    coffee = Coffee.objects.all()
    return render(request, 'coffee.html', {"coffees": coffee})