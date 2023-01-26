import markdown2
import secrets
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import util
from markdown2 import Markdown


class NewEntryForm(forms.Form):
    title = forms.CharField(label="New Entry")
    content = forms.CharField()
    edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdowner = Markdown()
    entryPage = util.get_entry(entry)
    if entryPage is None:
        return render(request, "encyclopedia/nonExistingEntry.html", {
            "entryTitle": entry
        })
    else: 
        return render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(entryPage),
            "entryTitle": entry
        })
