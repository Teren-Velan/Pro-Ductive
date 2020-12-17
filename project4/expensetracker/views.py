from django.contrib import messages
from django.shortcuts import render
from .models import Expenses
from .forms import ExpenseForm
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.db.models import Sum
from datetime import datetime, timedelta

# Create your views here.

# display and add expenses


def dashboard(request):
    if request.method == "POST":
        form_data = ExpenseForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "successfully added Entry.")
        else:
            messages.error(request, "Entry Submission was unsuccesful.")
    entries = Expenses.objects.order_by('-notedate')
    form = ExpenseForm()
    context = {'entries': entries, "form": form}
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

    context = {'today': today, 'tc': tc,
               'yc': yc, "sc": sc, "thc": thc, 'yrc': yrc, 'form': form, "entries": entries}

    return render(request, "expensetracker/dashboard.html", context)


def edit_entry(request, id):
    entry = Expenses.objects.get(pk=id)
    if request.GET.get("del") == "true":
        entry.delete()
        return HttpResponseRedirect(reverse("expensetracker:dashboard"))
    elif request.method == "POST":
        form_data = ExpenseForm(request.POST, instance=entry)
        if form_data.is_valid():
            form_data.save()
            return HttpResponseRedirect(reverse("expensetracker:dashboard", args=(entry.id,)))

    form_instance = ExpenseForm(instance=entry)

    context = {'form_instance': form_instance, "entry": entry}
    return render(request, 'expensetracker/dashboard.html', context)


def date_range(request):
    if request.method == "POST":
        fd = request.POST['fromdate']
        td = request.POST['todate']

        expense = Expenses.objects.filter(
            Q(date__gte=fd) & Q(date__lte=td)).values('date').annotate(totaldaily=Sum('cost'))

        expense_count = Expenses.objects.filter(
            Q(date__gte=fd) & Q(date__lte=td)).count()

        expense_total = Expenses.objects.filter(
            Q(date__gte=fd) & Q(date__lte=td)).values('date').annotate(totaldaily=Sum('cost')).aggregate(Sum('totaldaily'))

        context = {'fd': fd, "td": td, "expense": expense,
                   "expense_count": expense_count, "expense_total": expense_total}
        return render(request, "expensetracker/range.html", context)
    return render(request, "expensetracker/range.html")
