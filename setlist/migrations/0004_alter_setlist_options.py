# Generated by Django 3.2 on 2022-07-10 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0003_auto_20220623_1223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setlist',
            options={'ordering': ['gig__date']},
        ),
    ]