from django.contrib import admin
from django.urls import path
from Students import views as v1
from Fees import views as v2
from Courses import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', v1.student_view),
    path('fees/', v2.fees_view),
    path('courses/', v3.courses_view)
]