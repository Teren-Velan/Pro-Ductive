from django.contrib import messages
from django.shortcuts import render
from .models import Entry
from .forms import EntryForm
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect


# display all entries / add entries
def index(request):
    if request.method == "POST":
        form_data = EntryForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "successfully added Entry.")
        else:
            messages.error(request, "Entry Submission was unsuccesful.")

    entries = Entry.objects.order_by('-date_posted')
    form = EntryForm()
    context = {'entries': entries, 'form': form}
    return render(request, 'diary/index.html', context)


# edit and delete event
def show_entry(request, id):
    entry = Entry.objects.get(pk=id)

    if request.GET.get("del") == "true":
        entry.delete()  # deletes on cat
        return HttpResponseRedirect(reverse("index"))

    elif request.method == "POST":
        form_data = EntryForm(request.POST, instance=entry)  # django
        if form_data.is_valid():  # django
            form_data.save()  # save data to db
            # particular page
            # redirect to the page with the id
            #  the "," at the end is part of the code
            return HttpResponseRedirect(reverse("show_entry", args=(entry.id,)))
    form = EntryForm(instance=entry)

    context = {"form": form, "entry": entry}
    return render(request, 'diary/entry.html', context)
