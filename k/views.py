from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    template = "home.html"
    context = {}
    return render(request, template, context)


def service(request):
    template = "service.html"
    context = {}
    return render(request, template, context)


def about(request):
    template = "about.html"
    context = {}
    return render(request, template, context)


def contacts(request):
    template = "contacts.html"
    context = {}
    return render(request, template, context)


def partners(request):
    template = "partners.html"
    context = {}
    return render(request, template, context)