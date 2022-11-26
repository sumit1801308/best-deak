# Generated by Django 3.2.6 on 2022-05-07 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestdealapp', '0008_auto_20220507_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='user',
        ),
        migrations.AddField(
            model_name='ads',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bestdealapp.profile'),
        ),
    ]
