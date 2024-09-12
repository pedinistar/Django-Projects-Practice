from django.urls import path
from . import views

urlpatterns = [
    path('cricket_news', views.cricket_view),
]
