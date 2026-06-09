# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ReportForm
from .models import OccurrenceModel
import json

from django.shortcuts import render

def occurrence_report(request):
    return render(request, "reports/occurrence_report.html")

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

    data = [
        {
            "lat": float(r.latitude),
            "lng": float(r.longitude),
            "type": r.event_type,
            "type_display": r.get_event_type_display(),
            "time": r.timestamp.isoformat()
        }
        for r in reports
    ]

    return render(request, "reports/occurrence_display.html", {
        "reports_json": json.dumps(data)
    })

def about(request):
    return JsonResponse({"success": True}, status=200)

def imprint(request):
    return JsonResponse({"success": True}, status=200)

def privacy(request):
    return JsonResponse({"success": True}, status=200)