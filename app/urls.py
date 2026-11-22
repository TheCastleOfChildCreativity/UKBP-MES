from django.contrib import admin
from django.urls import path, include

from app.views import index, detail

urlpatterns = [
    path('', index),
    path('detail', detail),
]
