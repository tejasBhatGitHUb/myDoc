from django.db import models
from django.urls import reverse
from doctors.models import Doctor
from patients.models import Patient
# Create your models here.

class Specialization(models.Model):
    title=models.CharField(unique=True,verbose_name="Title",max_length=50)
    des=models.CharField(max_length=200,verbose_name="Description")
    patients=models.ManyToManyField(Patient,verbose_name="Counsulting Patients")
    doctors=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Practicing Doctors")

    class Meta:
        verbose_name ="Specialization"
        verbose_name_plural = "Specialization"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})