# Generated by Django 5.0.7 on 2024-08-02 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('weight', models.IntegerField(verbose_name='Weight')),
                ('height', models.FloatField(verbose_name='Height')),
                ('prescription', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Prescription')),
                ('suggestion', models.CharField(blank=True, max_length=2500, null=True, verbose_name='Suggestion')),
                ('pdf_link', models.URLField()),
                ('doctor', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor', verbose_name='Doctor')),
                ('patient', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='patients.patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
    ]
