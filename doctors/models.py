import datetime
from django.template.defaultfilters import slugify
from django.db import models
from django.urls import reverse
from patients.models import Patient
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


Spec_choices=(('Allergist/Immunologist', 'Allergist/Immunologist'),
              ('Anesthesiologist', 'Anesthesiologist'),
              ('Cardiologist', 'Cardiologist'),
              ('Dermatologist', 'Dermatologist'),
              ('Endocrinologist', 'Endocrinologist'),
              ('Gastroenterologist', 'Gastroenterologist'),
              ('Hematologist', 'Hematologist'),
              ('Infectious Disease Specialist', 'Infectious Disease Specialist'),
              ('Internist', 'Internist'), ('Nephrologist', 'Nephrologist'),
              ('Neurologist', 'Neurologist'),
              ('Obstetrician/Gynecologist (OB/GYN)', 'Obstetrician/Gynecologist (OB/GYN)'),
              ('Oncologist', 'Oncologist'), ('Ophthalmologist', 'Ophthalmologist'),
              ('Orthopedic Surgeon', 'Orthopedic Surgeon'),
              ('Otolaryngologist (ENT)','Otolaryngologist (ENT)'),
              ('Pediatrician', 'Pediatrician'), ('Psychiatrist', 'Psychiatrist'),
              ('Pulmonologist', 'Pulmonologist'), ('Radiologist', 'Radiologist'),
              ('Rheumatologist', 'Rheumatologist'),
              ('Surgeon', 'Surgeon'), 
              ('Urologist', 'Urologist'))



class Doctor(models.Model):
    nmc_id=models.IntegerField(verbose_name="NMC ID",unique=True)
    name=models.CharField(max_length=100,verbose_name="Name")
    email=models.EmailField(max_length=100,verbose_name="Email", unique=True,)
    date_of_birth=models.DateField(verbose_name="Date of birth")
    registration_year=  models.DateField(verbose_name="Date of NMC registraion")
    slug=models.SlugField(max_length=240,editable=False)
    phone_number=models.CharField(verbose_name="Phone number",unique=True,
                                  validators=[RegexValidator(regex=r'(?:\+?91[-\s]?)?0?\d{10}',message="Enter the correct phone number")])
    password=models.CharField(verbose_name="Password")
    valid=models.BooleanField(verbose_name="Valid",default=False)
    
    class Meta:
        verbose_name ="Doctor"
        verbose_name_plural ="Doctors"
        # ord=['name']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Doctor.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.id}: {self.name}"

    def get_absolute_url(self):
        return reverse("Doctor_detail", kwargs={"slug":self.slug,"pk": self.pk})
    
    
