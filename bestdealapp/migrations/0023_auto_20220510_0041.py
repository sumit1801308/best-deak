# Generated by Django 3.2.6 on 2022-05-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestdealapp', '0022_ads_pictures'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='pictures',
            new_name='back_img',
        ),
        migrations.AddField(
            model_name='ads',
            name='front_img',
            field=models.ImageField(blank=True, null=True, upload_to='car_adds'),
        ),
        migrations.AddField(
            model_name='ads',
            name='int_img',
            field=models.ImageField(blank=True, null=True, upload_to='car_adds'),
        ),
        migrations.AddField(
            model_name='ads',
            name='ls_img',
            field=models.ImageField(blank=True, null=True, upload_to='car_adds'),
        ),
        migrations.AddField(
            model_name='ads',
            name='main_img',
            field=models.ImageField(blank=True, null=True, upload_to='car_adds'),
        ),
        migrations.AddField(
            model_name='ads',
            name='rs_img',
            field=models.ImageField(blank=True, null=True, upload_to='car_adds'),
        ),
    ]