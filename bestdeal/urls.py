"""bestdeal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from bestdealapp import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Welcome BestDeal Admin"
admin.site.site_title = "BestDeal Admin Portal"
admin.site.index_title = "BestDeal Admin Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='home'),
    path('aboutus/',views.aboutus,name='about'),
    path('contactus/',views.contactus,name='contact'),
    path('cars/',views.car,name='cars'),
    path('cartypes/',views.cartypes,name='cartypes'),
    path('signup/',views.signup,name='signup'),
    path('check_user_exists/',views.check_user_exists,name="check_user_exist"),
    path('dashboard/',views.dash,name='dashboard'),
    path('edit_profile/',views.edit,name='edit-prof'),
    path('change_password/',views.cpass,name='cpass'),
    path('my_ad/',views.add,name='adds'),
    path('new_add/',views.new_add,name='newadd'),
    path('ad_details/<int:id>',views.single_ad,name='ad_detail'),
    path('edit_ad',views.edit_ad,name='editad'),
    path('delete_ad/',views.delete_ad,name='delete_ad'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('logout/',views.user_logout,name='logout'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
