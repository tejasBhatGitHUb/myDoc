# Generated by Django 5.0.7 on 2024-08-07 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_alter_patient_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='slug',
            field=models.SlugField(editable=False, max_length=255),
        ),
    ]
