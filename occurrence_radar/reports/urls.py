# urls.py
from django.urls import path
from .views import occurrence_report, report_occurrence_api, occurrence_display

urlpatterns = [
    path('occurrence-report/', occurrence_report, name='occurrence_report'),
    path('occurrence-display/', occurrence_display, name='occurrence_display'),
    path("api/report-occurrence/", report_occurrence_api, name="report_occurrence_api"),
]