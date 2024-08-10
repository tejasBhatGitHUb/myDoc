from django.template.defaultfilters import slugify
from django.db import models
from django.urls import reverse
from patients.models import Patient
from doctors.models import Doctor
# Create your models here.
class Report(models.Model):
    patient=models.ForeignKey(Patient,verbose_name="Patient",
                             on_delete=models.CASCADE)
    slug=models.SlugField(max_length=240,editable=False)
    age=models.IntegerField(verbose_name="Age",editable=True)
    weight=models.IntegerField(verbose_name="Weight",editable=True)
    height=models.FloatField(verbose_name="Height",editable=True)
    doctor=models.ForeignKey(Doctor,verbose_name="Doctor",
                             on_delete=models.CASCADE)
    prescription=models.TextField(verbose_name="Prescription",
                                  null=True,blank=True,editable=True)
    suggestion=models.TextField(verbose_name="Suggestion",
                                null=True,blank=True,editable=True)
    pdf_link=models.URLField(editable=True)

    class Meta:
        verbose_name = ("Report")
        verbose_name_plural = ("Reports")
        indexes = [
            models.Index(fields=["doctor", "patient"]),
        ]
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Report.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.id} : {self.patient}"

    def get_absolute_url(self):
        return reverse("Report_detail", kwargs={"slug":self.slug,"pk": self.pk})
