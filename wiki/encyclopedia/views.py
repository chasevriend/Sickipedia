from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util

class NewEntryForm(forms.Form):
    form = forms.CharField(label="New Entry")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def add(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["entry"]
            # request.session["entries"] += [entry]
            # return HttpResponseRedirect(reverse, "encyclopedia/index.html")

        else:
            return render(request, "encyclopedia/add.html", {
                "form": form
            })

    return render(request, "encyclopedia/add.html", {
        "form": NewEntryForm()
    })

def random(request):
    return render(request, "encyclopedia/random.html", {
        "random": random
    })