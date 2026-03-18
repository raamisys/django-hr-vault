from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt

class EmployeeRecord(models.Model):
    employee_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    bank_account_number = encrypt(models.CharField(max_length=100))
    annual_salary = encrypt(models.DecimalField(max_digits=10, decimal_places=2))
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='employee_records'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_name} - {self.department}"