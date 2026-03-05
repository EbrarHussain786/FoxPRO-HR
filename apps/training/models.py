from django.db import models
from apps.employees.models import Employee


class Training(models.Model):
    title = models.CharField(max_length=120)
    schedule_date = models.DateField()
    course_details = models.TextField()
    enrolled_employees = models.ManyToManyField(Employee, blank=True)
    certification_required = models.BooleanField(default=False)
