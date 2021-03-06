# Generated by Django 3.1.13 on 2021-09-13 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.CharField(default='personal', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('upload_choices', models.CharField(choices=[('Active', 'Active'), ('Archieve', 'Archieve')], default='Active', max_length=20, verbose_name='Upload Type')),
                ('upload_image', models.ImageField(default='images/anc-logo.png', upload_to='images')),
                ('document', models.FileField(upload_to='documents')),
                ('current_url', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('Present', 'Present Address'), ('Home', 'Home'), ('Work', 'Work'), ('Permanent', 'Permanent Address'), ('Other', 'Other')], max_length=10)),
                ('address', models.TextField(blank=True, verbose_name='Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
