from expensetracker.models import Expenses
from todo.models import List
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.db.models import Sum
from datetime import datetime, timedelta
from todo.forms import ListForm  # Create your views here.


def index(request):
    today = datetime.now().date()
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")

    yesterday = today - timedelta(1)
    seven = today - timedelta(7)
    thirty = today - timedelta(30)
    year = today - timedelta(365)
    tc = Expenses.objects.filter(date=today).aggregate(Sum('cost'))
    yc = Expenses.objects.filter(date=yesterday).aggregate(Sum('cost'))
    sc = Expenses.objects.filter(
        date__gte=seven, date__lte=today).aggregate(Sum('cost'))
    thc = Expenses.objects.filter(
        date__gte=thirty, date__lte=today).aggregate(Sum('cost'))
    yrc = Expenses.objects.filter(
        date__gte=year, date__lte=today).aggregate(Sum('cost'))
    entries = Expenses.objects.order_by('-notedate')

    if request.method == "POST":
        form_data = ListForm(request.POST)
        if form_data.is_valid():
            form_data.save()

    todo_list = List.objects.all
    todo_form = ListForm()

    context = {'today': today, 'tc': tc,
               'yc': yc, "sc": sc, "thc": thc, 'yrc': yrc, "entries": entries, 'dt_string': dt_string, "todo_list": todo_list, 'todo_form': todo_form}
    return render(request, 'dashboard/index.html', context)


def delete(request, id):
    entry = List.objects.get(pk=id)
    entry.delete()

    return redirect('dashboard:index')


def cross(request, id):
    item = List.objects.get(pk=id)
    item.completed = True
    item.save()
    return redirect('dashboard:index')


def uncross(request, id):
    item = List.objects.get(pk=id)
    item.completed = False
    item.save()
    return redirect('dashboard:index')
