from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect, response
from django.urls import reverse

monthy_challenges={
    "january" : "Eat on jan",
    "february" : "Eat on feb",
    "march" : "Eat on mar",
    "april" : "Eat on apr",
    "may" : "Eat on may",
    "june" : "Eat on jun",
    "july" : "Eat on jul",
    "august" : "Eat on aug",
    "september" : "Eat on sep",
    "october" : "Eat on oct",
    "november" : "Eat on nov",
    "december" : "Eat on dec"
}


def monthly_challenge_by_number(request,month):
    months = list(monthy_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_month =months[month - 1]
    redirect_path = reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthy_challenge(request,month):
    try:
        challenge_text = monthy_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")    
 