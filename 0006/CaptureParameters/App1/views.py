from django.shortcuts import render, HttpResponse

# Create your views here.
def display_id(request, id):
  return HttpResponse(f"<h1>{id}</h1>")

def display_name(request, name):
  return HttpResponse(f"<h1>{name}</h1>")

def display_salary(request, salary):
  salary = float(salary)
  return HttpResponse(f"<h1>{salary}</h1>")