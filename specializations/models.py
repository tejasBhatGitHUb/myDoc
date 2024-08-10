from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from doctors.models import Doctor
from patients.models import Patient
# Create your models here.

class Specialization(models.Model):
    title=models.CharField(unique=True,verbose_name="Title",max_length=50)
    slug=models.SlugField(max_length=240,editable=False)
    des=models.CharField(max_length=200,verbose_name="Description")
    patients=models.ManyToManyField(Patient,verbose_name="Counsulting Patients")
    doctors=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Practicing Doctors")

    class Meta:
        verbose_name ="Specialization"
        verbose_name_plural = "Specialization"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Specialization.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Specialization_detail", kwargs={"slug":self.slug,"pk": self.pk})