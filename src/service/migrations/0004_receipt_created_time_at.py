# Generated by Django 2.0 on 2018-09-02 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20180902_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='created_time_at',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
