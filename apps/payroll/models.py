from django.db import models
from apps.employees.models import Employee


class SalaryStructure(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=12, decimal_places=2)
    mobile_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transport_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)


class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    overtime_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2)
    generated_at = models.DateTimeField(auto_now_add=True)
