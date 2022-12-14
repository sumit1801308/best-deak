# Generated by Django 3.2.6 on 2022-05-03 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bestdealapp', '0006_cars_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profiles/%D/%M/%Y')),
                ('contact_number', models.CharField(blank=True, max_length=10, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField(blank=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profile Table',
            },
        ),
    ]
