from django.shortcuts import render, HttpResponse

# Create your views here.
def wish_view(request):
  return HttpResponse("Welcome to Django Application")

def wish_me_view(request):
  return HttpResponse("Hi, June!")

def thank_you_view(request):
  return HttpResponse("Thanks BRUH!!")