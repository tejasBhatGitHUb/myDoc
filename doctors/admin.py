from typing import Any
from django.contrib import admin
from .forms import DoctorForm
from django.http import HttpRequest
from .models import Doctor
from specializations.models import Specialization
# Register your models here.

class SpecializationInline(admin.TabularInline):
    model=Specialization
    
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    exclude=['slug']
    form=DoctorForm
    inlines=[SpecializationInline]
    ordering=['-valid','name','id','email']
    list_display=['name','nmc_id','email','valid']
    search_fields=['name','email','nmc_id']
    fields=['nmc_id','registration_year','name','date_of_birth',
            'email','phone_number','password','valid',]
    def get_readonly_fields(self, request: HttpRequest, obj: Any | None = ...) -> list[str] | tuple[Any, ...]:
        if obj:
            return self.readonly_fields+('nmc_id','name','email',
                                         'date_of_birth','registration_year',
                                         'phone_number','slug')
        return self.readonly_fields