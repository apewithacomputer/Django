from django.urls import path, include
from . import views

urlpatterns = [
    path('classes/', views.classApi, name="class"),
    path('students/', views.studentApi, name="student"),
]
