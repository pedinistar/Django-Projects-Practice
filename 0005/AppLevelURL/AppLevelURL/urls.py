from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CricketNewsApp/', include('CricketNewsApp.urls')),
    path('HockeyNewsApp/', include('HockeyNewsApp.urls')),
    path('TechNewsApp/', include('TechNewsApp.urls')),
]
