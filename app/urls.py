from django.contrib import admin
from django.urls import path, include
from app.views import index, details, history_operation, stages, work_pieces

urlpatterns = [
    path("", index),
    path("details/", details),
    path("history/", history_operation),
    path("stages/", stages),
    path("work_pieces/", work_pieces),
]
