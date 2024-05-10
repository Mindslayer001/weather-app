from django.urls import path, include
from .views import getInput, postWeather
urlpatterns = [
    path("", getInput, name="get_input")
]