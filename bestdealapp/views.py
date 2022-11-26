
from ast import Add
from multiprocessing import context
import profile
from pyexpat import model
from turtle import color
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from bestdealapp.models import address, cartype,profile,ads, conatact_number,address  
from django.conf import settings
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.models import User 

# Create your views here.
def homepage(request):
    # login form
    context = {}
    if request.method=="POST":
        eml = request.POST.get('email')
        psw = request.POST.get('pass')

        check_user = authenticate(username = eml, password = psw)
        if check_user:
            login(request,check_user)
            if check_user.is_superuser or check_user.is_staff:
                return HttpResponseRedirect('/admin')
            return  HttpResponseRedirect('/dashboard')
        else:
            context.update({'status':'Invalid login details','class':'alert-danger'})
    return render(request,'homepage.html',context)

def contactus(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'about.html')

def car(request):
    context = {}
    car = ads.objects.all()

    if "q" in request.GET:
        id = request.GET.get("q")
        car = ads.objects.filter(car_type = id)
        context['car_type'] = cartype.objects.get(id = id).name
    
    context.update({'cars':car})

    return render(request,'cars.html',context)

def cartypes(request):
    context = {}
    c = cartype.objects.all().order_by('id')
    context['cartypes'] = c
    return render(request,'cartypes.html',context)

def signup(request):
    context = {}
    if request.method == "POST":
        firstname = request.POST.get("fname")
        lastname = request.POST.get("lname")
        usname = request.POST.get("email")
        date = request.POST.get("dob")
        mobile = request.POST.get("number")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        gend = request.POST.get("radio")
        check = User.objects.filter(username = usname)
        if len(check)==0:
            usr = User.objects.create_user(usname,email,password)
            usr.first_name = firstname
            usr.last_name = lastname
            usr.save()
            Profile = profile(user=usr, contact_number = mobile, dob=date , gender = gend)
            Profile.save()  
            cont_num = conatact_number(user = usr, contact_number = mobile)
            cont_num.save()
            context['status'] = "User Regsitered Successfully"
        else:
            context['error'] = "This email is already registered with us"
    return render(request,'register.html',context)

def check_user_exists(request):
    usname = request.GET.get('usern')
    check = User.objects.filter(username=usname)
    if len(check)==0:
        return JsonResponse({'status':0,'message':'Not Existt!!'})
    else:
        return JsonResponse({'status':1,'message':'A user with this username is already exist!'})

def dash(request):
    context = {}
    login_user = get_object_or_404(User, id=request.user.id)
    Profile = profile.objects.get(user__id = request.user.id)
    context['profile'] = Profile
    return render(request,'dashboard.html',context)
    
def edit(request):
    context = {}
    login_user = get_object_or_404(User, id=request.user.id)
    Profile = profile.objects.get(user__id = request.user.id)
    Address = address.objects.get(user__id = request.user.id)
    context['profile'] = Profile
    if "update_profile" in request.POST:
        # print("file=",request.FILES)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        mobile = request.POST.get('contact_number')
        add = request.POST.get('address')
    
        Profile.user.first_name = fname
        Profile.user.last_name = lname
        Profile.user.save()

        Profile.contact_number = mobile
        Profile.address = add
        profile.address = add

        if "profile_pic" in request.FILES:
            pic = request.FILES['profile_pic']
            Profile.profile_pic = pic       
        Profile.save()  
        check = address.objects.filter(user = login_user)
        if len(check)==0:   
            Address.user = login_user
            Address.location = add
            Address.save()
        else:
            Address.location = add
            Address.save()
        context['status'] = 'profile updated successfulyy !!'
    return render(request,'edit_profile.html',context)

def edit_ad(request):
    context = {}
    login_user = get_object_or_404(User, id=request.user.id)
    ad = ads.objects.get(seller = login_user)
    context['add'] = ad
    if "update_profile" in request.POST:
        adname = request.POST.get('car_name')
        prc = request.POST.get('price')
        detail = request.POST.get('car_detail')

        ad.car_name = adname
        ad.price = prc
        ad.car_discription = detail

        if "main_pic" in request.FILES:
            pic1 = request.FILES['main_pic']
            ad.main_img = pic1 
        if "front_pic" in request.FILES:
            pic2 = request.FILES['front_pic']
            ad.front_img = pic2    
        if "back_pic" in request.FILES:
            pic3 = request.FILES['back_pic']
            ad.back_img = pic3 
        if "left_pic" in request.FILES:
            pic4 = request.FILES['left_pic']
            ad.ls_img = pic4 
        if "right_pic" in request.FILES:
            pic5 = request.FILES['right_pic']
            ad.rs_img = pic5 
        if "int_pic" in request.FILES:
            pic6 = request.FILES['int_pic']
            ad.int_img = pic6 
        
        ad.save()
        context['status'] = 'Add is updated successfulyy !!'
    return render(request,'edit_ad.html',context)

def cpass(request):
    context = {}
    login_user = get_object_or_404(User, id=request.user.id)
    Profile = profile.objects.get(user__id = request.user.id)
    context['profile'] = Profile
    if "change_pass" in request.POST:
        c_password = request.POST.get("current_password")
        n_password = request.POST.get("new_password")
        check = login_user.check_password(c_password)
        if check == True:
            login_user.set_password(n_password)
            login_user.save()
            login(request, login_user)
            context.update({'message':'Password is changed successfully', 'class':'alert-success'})
        else:
            context.update({'message':'Old Password is not matched !!!', 'class':'alert-danger'})
    return render(request,'change_pass.html',context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def delete(request,id):
    context = {}
    ad = get_object_or_404(ads,id=id)
    ad.delete()
    if request.method == "POST":
        context['status'] = "User Regsitered Successfully"
    return HttpResponseRedirect('/dashboard')

def delete_ad(request):
    context = {}
    adds = ads.objects.filter(seller = request.user.username).order_by('-id')
    context['adds'] = adds
    return render(request,'delete_ad.html',context)

def add(request):
    context = {}
    adds = ads.objects.filter(seller = request.user.username).order_by('-id')
    context['adds'] = adds
    return render(request,'my_ads.html',context)

def new_add(request):
    context = {}
    # nd = ads.objects.get(seller__id = request.user.id)
    # context['newadd'] = nd
    if request.method == "POST":
        sellr = profile.objects.get(user__id=request.user.id)
        contact = conatact_number.objects.get(user__id = request.user.id)
        adr = address.objects.get(user__id = request.user.id)
        carname = request.POST.get("carname")
        carbrand = request.POST.get("carbrand")
        carmodel = request.POST.get("carmodel")
        regyear = request.POST.get("regyear")
        km = request.POST.get("kilometers")
        fuel = request.POST.get("fueltype")
        cartype = request.POST.get("cartype")
        trans = request.POST.get("transmission")
        mil = request.POST.get("mileage")
        loc = request.POST.get("location")
        color = request.POST.get("color")
        cd = request.POST.get("cardetails")
        pr = request.POST.get("price")
        main_pic = request.FILES.get("images")

        newad = ads(
        user = sellr,seller = sellr,contact_number = contact,address=adr,car_name = carname, car_company = carbrand , car_model = carmodel, registration_year = regyear,
        fuel_type = fuel, mileage = mil, transmission = trans, location = loc, color = color, kilometers = km,
        car_discription = cd, car_type = cartype, price = pr , main_img = main_pic, )            
        newad.save()
        context['status'] = "Add is uploaded successfully !!"
    return render(request,'new_add.html',context)

def single_ad(request,id):
    context = {}
    s_ad = get_object_or_404(ads,id=id)
    context['sad'] = s_ad
    if request.user.is_authenticated:
        Profile = profile.objects.get(user__id = request.user.id)
        context['profile'] = Profile
    return render(request,'ad.html',context)

