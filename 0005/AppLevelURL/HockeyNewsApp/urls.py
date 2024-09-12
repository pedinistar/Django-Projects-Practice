from django.urls import path
from . import views

urlpatterns = [
    path('hockey_news', views.hockey_view)
]
