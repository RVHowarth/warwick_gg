# Generated by Django 2.2.1 on 2019-05-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uwcs_auth', '0007_warwickgguser_league_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warwickgguser',
            name='league_user',
            field=models.CharField(blank=True, max_length=32, verbose_name='Summoner name'),
        ),
    ]
