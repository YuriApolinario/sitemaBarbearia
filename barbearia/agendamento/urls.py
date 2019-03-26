from django.urls import path
from .views import *


urlpatterns = [
    path('inicio/', IndexView.as_view(), name="index"),
]
