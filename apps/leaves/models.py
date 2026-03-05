from django.db import models
from apps.employees.models import Employee


class LeaveRequest(models.Model):
    LEAVE_TYPES = [('annual', 'Annual'), ('sick', 'Sick'), ('casual', 'Casual')]
    STATUS = [('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    approved_by = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
