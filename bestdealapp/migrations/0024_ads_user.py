# Generated by Django 3.2.6 on 2022-05-13 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bestdealapp', '0023_auto_20220510_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
