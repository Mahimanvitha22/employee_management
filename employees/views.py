from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import EmployeeForm
from .models import Employee


@login_required
def dashboard(request):
    """Main dashboard showing key stats and recently added employees."""
    total_employees = Employee.objects.count()
    recent_employees = Employee.objects.order_by('-created_at')[:5]

    thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
    new_this_month = Employee.objects.filter(created_at__gte=thirty_days_ago).count()

    department_count = Employee.objects.values('department').distinct().count()

    context = {
        'total_employees': total_employees,
        'recent_employees': recent_employees,
        'new_this_month': new_this_month,
        'department_count': department_count,
    }
    return render(request, 'employees/dashboard.html', context)


@login_required
def employee_list(request):
    """List all employees with pagination and column sorting."""
    employees = Employee.objects.all()

    sort_by = request.GET.get('sort', '-created_at')
    allowed_sorts = [
        'name', '-name', 'employee_id', '-employee_id',
        'department', '-department', 'joining_date', '-joining_date',
        'salary', '-salary', '-created_at', 'created_at',
    ]
    if sort_by in allowed_sorts:
        employees = employees.order_by(sort_by)

    per_page = getattr(settings, 'EMPLOYEES_PER_PAGE', 10)
    paginator = Paginator(employees, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'total_employees': employees.count(),
        'current_sort': sort_by,
    }
    return render(request, 'employees/employee_list.html', context)


@login_required
def employee_add(request):
    """Add a new employee."""
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            messages.success(request, f"Employee '{employee.name}' ({employee.employee_id}) added successfully.")
            return redirect('employee_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_add.html', {'form': form})


@login_required
def employee_update(request, pk):
    """Update an existing employee."""
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, f"Employee '{employee.name}' updated successfully.")
            return redirect('employee_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_update.html', {'form': form, 'employee': employee})


@login_required
def employee_delete(request, pk):
    """Delete an employee after confirmation."""
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        name = employee.name
        emp_id = employee.employee_id
        employee.delete()
        messages.success(request, f"Employee '{name}' ({emp_id}) deleted successfully.")
        return redirect('employee_list')
    return render(request, 'employees/employee_delete.html', {'employee': employee})


@login_required
def employee_search(request):
    """Search employees by Employee ID, Name, or Department."""
    query = request.GET.get('q', '').strip()
    results = Employee.objects.none()

    if query:
        results = Employee.objects.filter(
            Q(employee_id__icontains=query) |
            Q(name__icontains=query) |
            Q(department__icontains=query)
        ).order_by('-created_at')

    per_page = getattr(settings, 'EMPLOYEES_PER_PAGE', 10)
    paginator = Paginator(results, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'page_obj': page_obj,
        'result_count': results.count() if query else None,
    }
    return render(request, 'employees/employee_search.html', context)


def custom_404(request, exception=None):
    """Custom 404 error page."""
    return render(request, '404.html', status=404)
