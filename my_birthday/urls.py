from django.urls import path
from . import views


app_name = "birthday"
urlpatterns = [
    path("", views.birthday_check_view, name="index"),
]
