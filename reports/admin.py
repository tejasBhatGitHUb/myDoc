from typing import Any
from django.http import HttpRequest
from django.contrib import admin
from .models import Report
# Register your models here.


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    ordering=['doctor']
    fields=['doctor','patient','age',
            'weight','height','prescription',
            'suggestion','pdf_link']
    def get_readonly_fields(self, request:HttpRequest, obj: Any|None=...)->list[str]| tuple[Any,...]:
        
        if obj:  
            return self.readonly_fields + ('doctor','patient')
        return self.readonly_fields
    