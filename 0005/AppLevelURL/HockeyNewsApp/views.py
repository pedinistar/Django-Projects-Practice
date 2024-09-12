from django.shortcuts import render, HttpResponse

# Create your views here.
def hockey_view(request):
  return HttpResponse("Hockey News")