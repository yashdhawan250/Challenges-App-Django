from django.urls import path

from . import views

urlpatterns=[
    path(""),
    path("<int:month>",views.monthly_challenge_by_number),
    path("<str:month>",views.monthy_challenge,name="month-challenge")
]