# Generated by Django 2.2.1 on 2019-05-16 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0035_auto_20190516_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='signup_end',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='signup_form',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='signup_start',
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_platform',
            field=models.CharField(choices=[('S', 'Steam'), ('B', 'Battle.NET'), ('L', 'League of Legends'), ('O', 'Other')], default='O', help_text='If "other" please specify', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_platform_other',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.CreateModel(
            name='TournamentSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField(blank=True, default='', max_length=1024)),
                ('platform_tag', models.CharField(max_length=64)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Tournament')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]