from django.contrib import admin
from .models import OccurrenceModel, EventType


admin.site.register(OccurrenceModel)
admin.site.register(EventType)
