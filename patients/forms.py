from django import forms
from django.contrib import admin
from .models import Patient


class PatientForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(PatientForm, self).__init__(*args, **kwargs)

    #     # Ensure that data is a regular Python dictionary so we can
    #     # modify it later.
    #     if isinstance(self.data, QueryDict):
    #         self.data = self.data.copy()

    #     # We assume here that the slug is only generated once, when
    #     # saving the object. Since they are used in URLs they should
    #     # not change when valid.
    #     if not self.instance.pk and self.data.get('name'):
    #         self.data['slug'] = slugify(self.data['name'])

    class Meta:
        model = Patient
        exclude=['slug']
        
class PatientAdmin(admin.ModelAdmin):
    exclude=['slug']
    form=PatientForm