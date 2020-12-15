from expensetracker.models import Expenses
from django.shortcuts import render
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.db.models import Sum
from datetime import datetime, timedelta  # Create your views here.


def index(request):
    today = datetime.now().date()

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

    context = {'today': today, 'tc': tc,
               'yc': yc, "sc": sc, "thc": thc, 'yrc': yrc, "entries": entries}
    return render(request, 'dashboard/index.html', context)
