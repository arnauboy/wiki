import markdown2
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import random

from django.urls import reverse
from pip._internal.utils import logging

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), "random_item": random.choice(util.list_entries()), "name": "css"
    })


def entry(request, name):
    try:
        html = markdown2.markdown(util.get_entry(name))
        entries = util.list_entries(),
        random_item = entries[0]
        random_item = random.choice(random_item)
        return render(request, "encyclopedia/entry.html", {"name": name.capitalize(), "content":
            html, "entries": entries, "random_item": random_item, "name": "css"})
    except:
        return render(request, "encyclopedia/pageNotFound.html")


def search(request):
    name = request.GET["q"].lower().capitalize()
    print(name)
    return redirect("entry", name=name)
