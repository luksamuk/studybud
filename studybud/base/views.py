from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def room(request: HttpRequest) -> HttpResponse:
    return render(request, "room.html")
