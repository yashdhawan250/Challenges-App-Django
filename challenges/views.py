from typing import List
from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect,response
from django.urls import reverse
from django.template.loader import render_to_string


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
    "december" : None
}

def index(request):
    list_items = ""
    months = list(monthy_challenges.keys())

    return render(request,"challenges/index.html",{
        "months": months
    })

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
        return render(request,"challenges/challenge.html",{
            "text" : challenge_text,
            "month_name":month.capitalize()
        })
    except:
        raise Http404()