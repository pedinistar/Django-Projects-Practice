from django.shortcuts import render, HttpResponse

# Create your views here.
def courses_view(request):
  return HttpResponse("<h1>Hello You are in the Courses Section of Project3</h1>")