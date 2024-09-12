from django.shortcuts import render, HttpResponse

# Create your views here.
def fees_view(request):
  return HttpResponse("<h1>Hello You are in the Fees Section of Project3</h1>")