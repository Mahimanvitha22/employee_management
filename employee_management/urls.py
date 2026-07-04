"""
URL configuration for employee_management project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

handler404 = 'employees.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='dashboard', permanent=False)),
    path('', include('employees.urls')),
]
