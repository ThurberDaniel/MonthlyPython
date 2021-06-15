from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthDictionary = {
    "January": "Shovel Snow New Year",
    "Febuary": " Valentines Day",
    "March": "St Partricks Day",
    "April": "Rainy",
    "May": "Memorial Day",
    "June": "Summer Time",
    "July": "Fourth of July",
    "August": "Slowly Fall",
    "September": "Fall Time",
    "October": "Halloween",
    "November": "Thanksgiving",
    "December": "Christmas",
}


def index(request):
    return HttpResponse("hello, Im working")


def monthly_challenge_by_number(request, month):
    months = list(monthDictionary.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    forward_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + forward_month)


def monthly_challenge(
    try:
        challenge_text = monthDictionary[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This Month is not supported")
