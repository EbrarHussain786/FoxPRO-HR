from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Designation(models.Model):
    title = models.CharField(max_length=120)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Employee(models.Model):
    STATUS_CHOICES = [('active', 'Active'), ('resigned', 'Resigned'), ('terminated', 'Terminated')]
    full_name = models.CharField(max_length=150)
    cnic = models.CharField(max_length=30, unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    joining_date = models.DateField()
    basic_salary = models.DecimalField(max_digits=12, decimal_places=2)
    emergency_contact_name = models.CharField(max_length=120)
    emergency_contact_phone = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.full_name
