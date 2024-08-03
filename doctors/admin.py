from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Doctor
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    ordering=['id',]
    fields=['nmc_id','registration_year','name','date_of_birth',
            'email','phone_number','password','valid']
    def get_readonly_fields(self, request: HttpRequest, obj: Any | None = ...) -> list[str] | tuple[Any, ...]:
        if obj:
            return self.readonly_fields+('nmc_id','name','email',
                                         'date_of_birth','registration_year',
                                         'phone_number')
        return self.readonly_fields