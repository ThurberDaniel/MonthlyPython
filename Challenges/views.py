from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views

monthDictionary = {
    "january": "Shovel Snow New Year",
    "febuary": " Valentines Day",
    "march": "St Partricks Day",
    "april": "Rainy",
    "may": "Memorial Day",
    "june": "Summer Time",
    "july": "Fourth of July",
    "august": "Slowly Fall",
    "september": "Fall Time",
    "october": "Halloween",
    "november": "Thanksgiving",
    "december": "Christmas",
}


def index(request):
    list_items = ""
    months = list(monthDictionary.keys())
    for month in months:
        capitalized = month.capitalize()
        path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{path}\">{capitalized}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


# def index(request):
#     return HttpResponse("hello, Im working")


def monthly_challenge_by_number(request, month):
    months = list(monthDictionary.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    forward_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthDictionary[month]
        response_data = render_to_string("Templates/index.html")
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("<h1>This Month is not supported</h1>")
