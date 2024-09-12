from django.urls import path
from . import views

urlpatterns = [
    path('display_id/<int:id>/', views.display_id),
    path('display_name/<str:name>/', views.display_name),
    path('display_salary/<str:salary>/', views.display_salary)
]