# Generated by Django 3.2.6 on 2022-05-13 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestdealapp', '0028_alter_conatact_number_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='contact_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bestdealapp.conatact_number'),
        ),
    ]
