from contextlib import nullcontext
from distutils.command.upload import upload
from hashlib import blake2b
from operator import truediv
from pydoc import locate
from tokenize import blank_re
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, NullBooleanField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from functools import update_wrapper

# Create your models here.
class cartype(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='cartype',blank = True)
    added_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = "profiles/%D/%M/%Y", null=True,blank=True)
    contact_number = models.CharField(max_length=10,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    address = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural="Profile Table"

class conatact_number(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    contact_number = models.CharField(max_length = 10, null = True)

    def __str__(self):
        return self.contact_number

    class Meta:
        verbose_name_plural="Contact Table"

class address(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    location = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural="Address Table"

class ads(models.Model):
    user = models.OneToOneField(profile, on_delete=models.CASCADE,null=True,unique=False)
    seller = models.CharField(max_length= 200,null=True,blank=True,unique=False)
    contact_number = models.ForeignKey(conatact_number,on_delete=models.CASCADE,null=True)
    address = models.ForeignKey(address,on_delete=models.CASCADE,null=True)
    car_type = models.IntegerField(null=True,blank=True)
    car_name = models.CharField(max_length= 200,null=True,blank=True)
    car_company = models.CharField(max_length=50,null=True,blank=True)
    car_model = models.CharField(max_length=10,null=True,blank=True)
    registration_year = models.CharField(max_length=10,null=True,blank=True)
    kilometers = models.CharField(max_length=10,null=True,blank=True)
    fuel_type = models.CharField(max_length=10,null=True,blank=True)
    mileage = models.CharField(max_length=10,null=True,blank=True)
    transmission = models.CharField(max_length=10,null=True,blank=True)
    location = models.CharField(max_length=20,null=True,blank=True)
    color = models.CharField(max_length=15,null=True,blank=True)
    car_discription = models.TextField(blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    main_img = models.ImageField(upload_to="car_adds",null=True,blank=True)
    front_img = models.ImageField(upload_to="car_adds",null=True,blank=True)
    back_img = models.ImageField(upload_to="car_adds",null=True,blank=True)
    ls_img = models.ImageField(upload_to="car_adds",null=True,blank=True)
    rs_img = models.ImageField(upload_to="car_adds",null=True,blank=True)
    int_img = models.ImageField(upload_to="car_adds",null=True,blank=True)
    added_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.seller

    class Meta:
        verbose_name_plural="Ads Table"