# Generated by Django 3.2 on 2022-06-30 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_gig_image_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gig',
            name='image',
        ),
        migrations.RemoveField(
            model_name='gig',
            name='image_status',
        ),
    ]
