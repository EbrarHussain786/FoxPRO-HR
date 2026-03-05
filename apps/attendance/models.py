from django.db import models
from apps.employees.models import Employee


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    late_minutes = models.PositiveIntegerField(default=0)
    overtime_minutes = models.PositiveIntegerField(default=0)
    device_fingerprint = models.CharField(max_length=120, blank=True)
    gps_coordinates = models.CharField(max_length=120, blank=True)

    class Meta:
        unique_together = ('employee', 'date')
