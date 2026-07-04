from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'employee_id', 'name', 'email', 'phone',
        'department', 'designation', 'salary', 'joining_date', 'created_at',
    )
    list_filter = ('department', 'joining_date', 'created_at')
    search_fields = ('employee_id', 'name', 'email', 'phone')
    ordering = ('-created_at',)
    readonly_fields = ('employee_id', 'created_at', 'updated_at')
    list_per_page = 25

    fieldsets = (
        ('Identification', {
            'fields': ('employee_id', 'name', 'email', 'phone')
        }),
        ('Employment Details', {
            'fields': ('department', 'designation', 'salary', 'joining_date')
        }),
        ('Additional Information', {
            'fields': ('address',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
