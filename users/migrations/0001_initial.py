# Generated by Django 3.1.13 on 2021-09-13 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('choose', 'Choose'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.'), ('Prof.', 'Prof.'), ('__', 'Other.')], default='choose', max_length=6)),
                ('job_title', models.CharField(blank=True, default='', max_length=40, verbose_name='Job Title')),
                ('user_type', models.CharField(choices=[('Permanent', 'Permanent'), ('Contractor', 'Contractor')], default='Permanent', max_length=10, verbose_name='Employment Type')),
                ('summary', models.TextField(blank=True, verbose_name='Summary')),
                ('other_names', models.CharField(blank=True, default='', max_length=200, verbose_name='Other Names')),
                ('nick_name', models.CharField(blank=True, default='', max_length=200, verbose_name='Nick Names')),
                ('image', models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')),
                ('phone1', models.CharField(blank=True, max_length=20, verbose_name='Work Phone')),
                ('phone2', models.CharField(blank=True, max_length=20, verbose_name='Personal Phone')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('email2', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Company Email')),
                ('location', models.CharField(blank=True, default='', max_length=25, verbose_name='Current Location')),
                ('skills_have', models.TextField(blank=True, verbose_name='Skills I Have')),
                ('skills_like2_have', models.TextField(blank=True, verbose_name='Skills I Would Like To Have')),
                ('timezone', models.CharField(blank=True, default='', max_length=25, verbose_name='Time Zone')),
                ('zip_post_code', models.CharField(blank=True, default='', max_length=25, verbose_name='Zip/Post Code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
