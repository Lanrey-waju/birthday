from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def birthday_check(request):
    return render(
        request,
        "birth/index.html",
        {
            "birthday": date.today() == date(date.today().year, 12, 27),
            "countdown": date(date.today().year, 12, 27) - date.today(),
        },
    )
