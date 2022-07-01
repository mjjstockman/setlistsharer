# Generated by Django 3.2 on 2022-07-01 09:04

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220630_0846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gig',
            options={},
        ),
        migrations.AddField(
            model_name='gig',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='gig',
            name='featured_image_status',
            field=models.IntegerField(choices=[(0, 'No Image'), (1, 'Waiting Confirmation'), (2, 'Published')], default=0),
        ),
    ]
