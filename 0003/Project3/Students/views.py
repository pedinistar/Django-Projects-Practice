from django.shortcuts import render, HttpResponse

# Create your views here.
def student_view(request):
  return HttpResponse("<h1>Hello You are in the Students Section of Project3</h1>")