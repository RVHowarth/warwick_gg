# Generated by Django 2.0.2 on 2018-06-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_eventsignup_photography_consent'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='LIB2', max_length=100),
            preserve_default=False,
        ),
    ]
