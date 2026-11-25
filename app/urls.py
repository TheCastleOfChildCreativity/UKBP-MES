from idlelib import history

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index),
    path("details/", views.details),
    path("history/", views.history_operation),
    path("stages/", views.stages),
    path("work_pieces/", views.work_pieces),
]
