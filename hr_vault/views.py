from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import EmployeeRecord

@login_required
def add_employee(request):
    if request.method == 'POST':
        employee_name = request.POST.get('employee_name')
        department = request.POST.get('department')
        bank_account_number = request.POST.get('bank_account_number')
        annual_salary = request.POST.get('annual_salary')

        EmployeeRecord.objects.create(
            employee_name=employee_name,
            department=department,
            bank_account_number=bank_account_number,
            annual_salary=annual_salary,
            added_by=request.user
        )
        return redirect('employee_list')

    return render(request, 'hr_vault/add_employee.html')

@login_required
def employee_list(request):
    records = EmployeeRecord.objects.all()
    return render(request, 'hr_vault/employee_list.html', {'records': records})