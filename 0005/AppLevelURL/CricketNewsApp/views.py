from django.shortcuts import render, HttpResponse

# Create your views here.
def cricket_view(request):
  return HttpResponse("Cricket News")