from django.urls import path
from .views import JobCreateAPIView, JobDetailAPIView

urlpatterns = [
    path("jobs/", JobCreateAPIView.as_view()),
    path("jobs/<int:pk>/", JobDetailAPIView.as_view()),
]
