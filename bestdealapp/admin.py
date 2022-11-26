from django.contrib import admin

from bestdealapp.models import  address, cartype, profile , ads,conatact_number,address

# Register your models here.
class cartypeAdmin(admin.ModelAdmin):
    list_display=['id','name','image','added_on','updated_on']

# class carsAdmin(admin.ModelAdmin):
#     list_display=['id','name','kilometers','price','added_on','updated_on']

class SignUpAdmin(admin.ModelAdmin):
    list_display=['id','user','updated_on']

class AdsAdmin(admin.ModelAdmin):
    list_display = ['id','seller','car_name']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','user','contact_number']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','user','location']


admin.site.register(cartype,cartypeAdmin)
# admin.site.register(cars,carsAdmin)
admin.site.register(profile,SignUpAdmin)
admin.site.register(ads,AdsAdmin)
admin.site.register(conatact_number,ContactAdmin)
admin.site.register(address,AddressAdmin)