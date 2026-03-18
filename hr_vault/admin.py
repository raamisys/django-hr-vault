from django.contrib import admin
from django.db import connection
from .models import EmployeeRecord

@admin.register(EmployeeRecord)
class EmployeeRecordAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'department', 'added_by', 'view_ciphertext')
    readonly_fields = ('created_at',)

    def view_ciphertext(self, obj):
        if obj.pk:
            table = EmployeeRecord._meta.db_table
            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT bank_account_number, annual_salary FROM {table} WHERE id = %s",
                    [obj.pk]
                )
                row = cursor.fetchone()
                if row:
                    bank = str(row[0])[:20]
                    salary = str(row[1])[:20]
                    return f"Bank: {bank}... | Salary: {salary}..."
        return "N/A"

    view_ciphertext.short_description = "Encrypted Data"