# Generated by Django 3.2 on 2022-07-01 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220701_1107'),
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