from django.db import models


class OccurrenceModel(models.Model):

    EVENT_TYPES = [
        ("paper_check", "Paper Check"),
        ("other", "Other"),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6) # 6 decimals is approx 10cm
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)

    def __str__(self):
        return f"{self.event_type} at ({self.latitude}, {self.longitude}) reported at {self.timestamp}"