from django.db import models
from django.urls import reverse
from patients.models import Patient
from doctors.models import Doctor
# Create your models here.
class Report(models.Model):
    patient=models.ForeignKey(Patient,verbose_name="Patient",
                             on_delete=models.CASCADE)
    age=models.IntegerField(verbose_name="Age",editable=True)
    weight=models.IntegerField(verbose_name="Weight",editable=True)
    height=models.FloatField(verbose_name="Height",editable=True)
    doctor=models.ForeignKey(Doctor,verbose_name="Doctor",
                             on_delete=models.CASCADE)
    prescription=models.CharField(max_length=1000,verbose_name="Prescription",
                                  null=True,blank=True,editable=True)
    suggestion=models.CharField(max_length=2500,verbose_name="Suggestion",
                                null=True,blank=True,editable=True)
    pdf_link=models.URLField(editable=True)

    class Meta:
        verbose_name = ("Report")
        verbose_name_plural = ("Reports")
        indexes = [
            models.Index(fields=["doctor", "patient"]),
        ]

    def __str__(self):
        return f"{self.patient.id} : {self.patient}"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
