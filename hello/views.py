from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # return HttpResponse("Hello, world!")
    return render(request, "hello/index.html")


def rama(request):
    return HttpResponse("Hello, Ramakrishna!")


def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")  # this actually makes our work lot more easy, and less tedious
    return render(request, "hello/greet.html", {"name": name.capitalize()})
