# Generated by Django 3.2.6 on 2022-05-13 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bestdealapp', '0031_alter_address_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='addres',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
