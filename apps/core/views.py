from django.shortcuts import render


def dashboard_view(request):
    metrics = {
        'total_employees': 128,
        'today_attendance': '115 / 128',
        'leave_requests': 7,
        'payroll_summary': '$184,000',
        'notifications': 12,
    }
    employee_widget = {
        'my_attendance': '22 / 24 days',
        'leave_balance': {'annual': 12, 'sick': 8, 'casual': 5},
        'latest_payslip': 'March 2026',
        'announcements': ['Performance review cycle starts next week.'],
    }
    modules = [
        'Employee Management', 'Attendance Management', 'Leave Management',
        'Payroll Management', 'Recruitment Management', 'Performance Management',
        'Training & Development', 'Document Management', 'Shift & Scheduling',
        'Reporting & Analytics', 'Roles & Permissions', 'Notification & Communication',
        'System Settings & Configuration',
    ]
    return render(request, 'dashboard/index.html', {
        'metrics': metrics,
        'employee_widget': employee_widget,
        'modules': modules,
    })


def specification_view(request):
    return render(request, 'dashboard/specification.html')


def implementation_guide_view(request):
    return render(request, 'dashboard/implementation_guide.html')
