from django.db import models

class EventType(models.Model):
    key = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class OccurrenceModel(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6) # 6 decimals is approx 10cm
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    event_type = models.ForeignKey(
        "EventType",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.event_type} at ({self.latitude}, {self.longitude}) reported at {self.timestamp}"