from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    slug = models.SlugField(max_length=255,editable=False)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=15)
    

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Patient.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}: {self.name}"

    def get_absolute_url(self):
        return reverse("Patient_detail", kwargs={"slug":self.slug,"pk": self.pk})
