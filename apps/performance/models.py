from django.db import models
from apps.employees.models import Employee


class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_period = models.CharField(max_length=100)
    kpi_score = models.DecimalField(max_digits=5, decimal_places=2)
    manager_feedback = models.TextField()
    self_assessment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
