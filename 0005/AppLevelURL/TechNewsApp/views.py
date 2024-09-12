from django.shortcuts import render, HttpResponse

# Create your views here.
def tech_view(request):
  return HttpResponse("Tech News")