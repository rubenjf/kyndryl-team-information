# Generated by Django 3.1.13 on 2021-09-13 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kyndril', '0002_auto_20210913_1029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='resident',
            new_name='user',
        ),
    ]