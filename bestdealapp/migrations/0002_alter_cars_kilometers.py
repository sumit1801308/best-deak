# Generated by Django 3.2.6 on 2022-05-01 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestdealapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='kilometers',
            field=models.IntegerField(),
        ),
    ]
