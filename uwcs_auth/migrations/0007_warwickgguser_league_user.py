# Generated by Django 2.2.1 on 2019-05-16 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uwcs_auth', '0006_auto_20190504_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='warwickgguser',
            name='league_user',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
