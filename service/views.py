from django.shortcuts import render, redirect
from . models import Demands
from django.views.generic import ListView, CreateView
from . forms import DemandForm
from django.contrib import messages
# Create your views here.


def service(request):
    template = "service.html"
    context = {}
    return render(request, template, context)


def new_demand(request):

    if request.method == 'POST':
        form = DemandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка записана в базу данных заявок. Мы вам перезвоним в ближайшее время.")
            return redirect('../')
        else:
            context = {'form': form}
            return render(request, 'service/new_demand.html', context)
    else:
        form = DemandForm()
        context = {'form': form}
        return render(request, 'service/new_demand.html', context)