# Generated by Django 5.0.7 on 2024-08-05 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specializations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='slug',
            field=models.SlugField(blank=True, max_length=120),
        ),
    ]
