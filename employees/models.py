from django.core.validators import RegexValidator, MinValueValidator
from django.db import models


class Employee(models.Model):
    """Represents an employee record in the system."""

    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('FINANCE', 'Finance'),
        ('MARKETING', 'Marketing'),
        ('SALES', 'Sales'),
        ('OPERATIONS', 'Operations'),
        ('LEGAL', 'Legal'),
        ('SUPPORT', 'Customer Support'),
    ]

    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    employee_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        help_text="Auto-generated unique employee identifier."
    )
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(validators=[phone_validator], max_length=17)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    joining_date = models.DateField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.employee_id} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.employee_id:
            last_employee = Employee.objects.order_by('id').last()
            next_id = (last_employee.id + 1) if last_employee else 1
            self.employee_id = f"EMP{next_id:04d}"
            # Ensure uniqueness even if an earlier record was deleted
            while Employee.objects.filter(employee_id=self.employee_id).exists():
                next_id += 1
                self.employee_id = f"EMP{next_id:04d}"
        super().save(*args, **kwargs)
