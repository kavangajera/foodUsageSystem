from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render, redirect
from .models import CustomUser,Volunteer_Detail,Donor_Detail,Donate_Money,Donate_Food
from django.contrib import messages
from datetime import datetime,date
from django.utils.dateparse import parse_date
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        role = request.POST['role']
        phone = request.POST['phone']
        #validations::
        
        if len(phone)>10 or len(phone)<10:
            messages.error(request,"invalid phone number")
            return redirect('homepage')
        
        if(password!=confirm_password):
            messages.error(request,"enter correct as above password")
            return redirect('homepage')
        user = CustomUser.objects.create_user(username=username, password=password, email=email, role=role,phone=phone)
        
        return redirect('login_view')  

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            if user.role == 'volunteer':
                request.session['user_username'] = user.username
                return redirect('volunteer')
            else:
                request.session['user_username'] = user.username
                return redirect('donator')
                 
        else:
            messages.success(request,"invalid credentials")
            return redirect('homepage')
    
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    messages.success(request,"logged OUT")
    return redirect('homepage')

def volunteer(request):
    if request.method == "POST":
       username = request.user.username
       phone = request.user.phone
       email = request.user.email
       city = request.POST.get('city')
       foodname = request.POST.get('foodname')
       qty = request.POST.get('qty')
       duedate = request.POST.get('duedate')
       custom_date = datetime.strptime(duedate, '%Y-%m-%d').date()
       vol = Volunteer_Detail(username=username,phone = phone,email=email,city=city,foodName=foodname,quantity=qty,duedate=custom_date)
       vol.save()
    return render(request,'volunteer.html')

def donator(request):
    if request.method == 'POST':
        username = request.user.username
        username = request.user.username
        phone = request.user.phone
        email = request.user.email
        city = request.POST.get('city')
        donor = Donor_Detail(username=username,phone = phone,email=email,city=city)
        donor.save()
    return render(request,'donator.html')

def money(request):
    
    if request.method == 'POST':
        donor = request.user.username
        volunteer = request.POST.get('vol')
        amount = request.POST.get('amount')
        reason = request.POST.get('reason')
        date = datetime.today()
        md = Donate_Money(donor=donor,volunteer=volunteer,amount=amount,reason=reason,date=date)
        md.save()
    donor_detail = Donor_Detail.objects.filter(username=request.user.username).first()
    get_city = donor_detail.city
    get_volunteers = Volunteer_Detail.objects.filter(city=get_city)
    return render(request,'money.html',{'get_volunteers': get_volunteers})

def food(request):
    if request.method == 'POST':
       donor = request.user.username
       volunteer = request.POST.get('vol')
       food_detail = Volunteer_Detail.objects.filter(username=volunteer).first()
       foodname = food_detail.foodName
       quantity = food_detail.quantity
       date = datetime.today()
       fd = Donate_Food(donor=donor,volunteer=volunteer,foodName=foodname,quantity=quantity,date=date)
       fd.save()
       food_detail.delete()
    donor_detail = Donor_Detail.objects.filter(username=request.user.username).first()
    get_city = donor_detail.city
    get_volunteers = Volunteer_Detail.objects.filter(city=get_city)
    
    return render(request,'food.html',{'get_volunteers': get_volunteers})   

def chooseDonate(request):
    return render(request,'donation_options.html')

def history(request):
    get_money_details = Donate_Money.objects.filter(volunteer=request.user.username)
    get_food_details = Donate_Food.objects.filter(volunteer=request.user.username)
    return render(request,'history.html',{'get_money_details': get_money_details , 'get_food_details':get_food_details})