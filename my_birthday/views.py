from django.shortcuts import render
from datetime import datetime, timedelta, date

# Create your views here.
def birthday_check(request):
    """Creste a view that checks if today is Abdulmumin's birthday (27th of December)"""
    birthday_today = False
    current_year = date.today().year
    birthday = date(current_year, 12, 27)
    if birthday==date.today():
        birthday_today = True
    days_remaining = (birthday - date.today()).days
    # days_remaining = days_remaining.days
    print(birthday, days_remaining)
    return render(
        request,
        "birth/index.html",
        {   
            "birthday_today": birthday_today,
            "birthday": birthday,
            "days_remaining": days_remaining,
        },
    )
