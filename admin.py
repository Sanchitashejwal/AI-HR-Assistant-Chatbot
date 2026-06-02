from django.contrib import admin
from .models import Resignation

@admin.register(Resignation)
class ResignationAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'employee_id', 'reason', 'timestamp']
