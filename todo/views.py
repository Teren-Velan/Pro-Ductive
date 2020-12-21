from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import List
from .forms import ListForm
from django.contrib import messages


# Create your views here.

def index(request):
    if request.method == "POST":
        form_data = ListForm(request.POST)
        if form_data.is_valid():
            form_data.save()

    entries = List.objects.all
    form = ListForm()
    context = {'entries': entries, 'form': form}
    return render(request, 'dashboard/index.html', context)


def delete(request, id):
    entry = List.objects.get(pk=id)
    entry.delete()
    return redirect('todo:index')


def cross(request, id):
    item = List.objects.get(pk=id)
    item.completed = True
    item.save()
    return redirect('todo:index')


def uncross(request, id):
    item = List.objects.get(pk=id)
    item.completed = False
    item.save()
    return redirect('todo:index')
