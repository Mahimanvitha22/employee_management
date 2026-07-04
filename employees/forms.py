from datetime import date

from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    """ModelForm for creating and updating Employee records with validation."""

    joining_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Employee
        fields = [
            'name', 'email', 'phone', 'department',
            'designation', 'salary', 'joining_date', 'address',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'name@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '+919876543210'
            }),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'designation': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'e.g. Senior Developer'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'e.g. 55000.00', 'step': '0.01'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3, 'placeholder': 'Enter full address'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        qs = Employee.objects.filter(email__iexact=email)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("An employee with this email already exists.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        digits = phone.replace('+', '')
        if not digits.isdigit():
            raise forms.ValidationError("Phone number must contain only digits and an optional leading '+'.")
        if len(digits) < 9 or len(digits) > 15:
            raise forms.ValidationError("Phone number must be between 9 and 15 digits.")
        return phone

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary is None:
            raise forms.ValidationError("Salary is required.")
        if salary <= 0:
            raise forms.ValidationError("Salary must be greater than zero.")
        if salary > 100000000:
            raise forms.ValidationError("Salary value is unrealistically high.")
        return salary

    def clean_joining_date(self):
        joining_date = self.cleaned_data.get('joining_date')
        if joining_date and joining_date > date.today():
            raise forms.ValidationError("Joining date cannot be in the future.")
        return joining_date

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name
