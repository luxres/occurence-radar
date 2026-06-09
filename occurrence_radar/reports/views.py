# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ReportForm
from .models import OccurrenceModel, EventType
import json

from django.shortcuts import render

def occurrence_report(request):
    event_types = EventType.objects.all()
    return render(request, "reports/occurrence_report.html", {
        "event_types": event_types
    })

def report_occurrence_api(request):
    if request.method == "POST":
        form = ReportForm(request.POST)

        if form.is_valid():
            obj = form.save()
            return JsonResponse({
                "success": True,
                "id": obj.id
            })

        # 🔥 IMPORTANT: return actual errors
        return JsonResponse({
            "success": False,
            "errors": form.errors
        }, status=400)

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)

def occurrence_display(request):
    reports = OccurrenceModel.objects.all()
    event_types = EventType.objects.all()

    data = [
        {
            "lat": float(r.latitude),
            "lng": float(r.longitude),
            "type": r.event_type.key,
            "type_display": r.event_type.label,
            "time": r.timestamp.isoformat()
        }
        for r in reports
    ]

    return render(request, "reports/occurrence_display.html", {
        "reports_json": json.dumps(data),
        "event_types": event_types
    })

def about(request):
    return JsonResponse({"success": True}, status=200)

def imprint(request):
    return JsonResponse({"success": True}, status=200)

def privacy(request):
    return JsonResponse({"success": True}, status=200)