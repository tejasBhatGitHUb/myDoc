from typing import Any
from django.http import HttpRequest
from django.contrib import admin
from . models import Patient
# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    ordering=["id"]
    fields=['name','email','password']
    def get_readonly_fields(self, request:HttpRequest, obj: Any | None = ...)-> list[str]| tuple[Any, ...]:
        if obj:  
            return self.readonly_fields + ('name','email',)
        return self.readonly_fields