# Generated by Django 2.0 on 2018-09-02 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_receipt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_name',
            new_name='name',
        ),
    ]
