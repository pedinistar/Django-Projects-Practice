from django.urls import path
from . import views

urlpatterns = [
    path('tech_news', views.tech_view),
]
