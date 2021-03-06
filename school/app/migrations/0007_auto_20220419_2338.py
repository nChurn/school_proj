# Generated by Django 3.2.6 on 2022-04-19 23:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220419_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='curator',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='presentation',
            field=models.FileField(blank=True, null=True, upload_to='projects/presentations', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pptx', 'ppt'])]),
        ),
    ]
