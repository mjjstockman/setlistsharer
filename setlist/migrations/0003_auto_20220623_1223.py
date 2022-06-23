# Generated by Django 3.2 on 2022-06-23 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('setlist', '0002_alter_gig_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='release',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='song',
            name='slug',
        ),
        migrations.AlterField(
            model_name='setlist',
            name='gig',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='setlist_gig', to='home.gig'),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.DeleteModel(
            name='Gig',
        ),
    ]
