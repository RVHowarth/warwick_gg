# Generated by Django 2.2.1 on 2019-05-16 10:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0037_auto_20190516_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='signup_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tournament',
            name='signup_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='signup_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
