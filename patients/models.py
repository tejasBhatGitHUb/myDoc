from django.db import models
from django.urls import reverse

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=15)
    

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        

    def __str__(self):
        return f"{self.id}: {self.name}"

    def get_absolute_url(self):
        return reverse("Patient_detail", kwargs={"pk": self.pk})
