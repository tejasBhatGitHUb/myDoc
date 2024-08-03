from typing import Any
from django.http import HttpRequest
from django.contrib import admin
from .models import Specialization
# Register your models here.
@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    ordering=['title']
    fields=['title','des','doctors','patients',]
    def get_readonly_fields(self, request: HttpRequest, obj: Any | None = ...) -> list[str] | tuple[Any, ...]:
        if obj:
            return self.readonly_fields+('title',)
        return self.readonly_fields