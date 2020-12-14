from django.contrib import messages
from django.shortcuts import render
from .models import Expenses
from .forms import ExpenseForm
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect


# Create your views here.

# display and add expenses
def index(request):
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
    return render(request, 'expensetracker/index.html', context)
