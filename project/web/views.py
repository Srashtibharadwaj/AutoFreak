from django.shortcuts import render,redirect
from .models import register
from .models import carrental
from .models import mechanic


# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    if request.method=="POST":
        name=request.POST['Name']
        contact=request.POST['Contact']
        email=request.POST['Email']
        password=request.POST['Password']
        register(name=name,contact=contact,email=email,password=password,user_type='user').save()
        message="registration done"
        return render(request,'signup.html',{'msg':message})
   

    return render(request,'signup.html')
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        if register.objects.filter(email=email,password=password):
            data=register.objects.filter(email=email,password=password).get()
            ut=data.user_type
            if ut=='admin':
                request.session['email']=email
                return redirect('admin_dashboard')
            
            else:
                request.session['email']=email
                return redirect('user_dashboard')
        else:
            msg="Invaild Date"
            return render(request,'login.html',{'msg':msg})
    return render(request,'login.html')
    

def user_dashboard(request):
    email=request.session['email']
    data=register.objects.filter(email=email).get()
    return render(request,'user/dashboard.html',{'data':data})
   
def user_booking(request):
     if request.method=="POST":
        pickuplocation=request.POST['pickuplocation']
        pickupdate=request.POST['pickupdate']
        pickuptime=request.POST['pickuptime']
        dropofflocation=request.POST['dropofflocation']
        dropoffdate=request.POST['dropoffdate']
        dropofftime=request.POST['dropofftime']
        
        carrental(pickuplocation=pickuplocation,pickupdate=pickupdate,pickuptime=pickuptime,dropofflocation=dropofflocation,
        dropoffdate=dropoffdate,dropofftime=dropofftime,).save()
        message=" booking done"
        return render(request,'user/dashboard.html',{'msg':message})
     return render(request,'user/booking.html')
def user_changepassword(request):
    email=request.session['email']
    if request.method=="POST":
       cpassword=request.POST['cpassword']
       npassword=request.POST['npassword']
       if register.objects.filter(email=email,password=cpassword):
           register.objects.filter(email=email).update(password=npassword)
           msg="your password is succesfully changed"
           return render(request,'user/changepassword.html',{'msg':msg})
       else:
           msg="wrong password entered"
           return render(request,'user/changepassword.html',{'msg':msg})
    return render(request,'user/changepassword.html')


def user_editprofile(request):
    return render(request,'user/editprofile.html')
def user_lasttrip(request):
    return render(request,'user/lasttrip.html')
def user_logout(request):
    return redirect('login')   
def user_editprofile(request):
    return render(request,'user/editprofile.html')
def admin_dashboard(request):
    data=register.objects.all()
    return render(request,'admin/dashboard.html',{'data':data})
def admin_addedoffers(request):
    data=carrental.objects.all()
    return render(request,'admin/addedoffers.html',{'data':data})
    
def admin_car(request):
    if request.method=="POST":
       name=request.POST['name']
       contact=request.POST['contact']
       email=request.POST['email']
       work_duration=request.POST['work_duration']
       salary=request.POST['salary']
       mechanic(name=name,contact=contact,email=email,work_duration=work_duration,salary=salary).save()
       message="mechanic added sucessfully"
       return render(request,'admin/car.html',{'msg':message})
    return render(request,'admin/car.html')
    
def admin_employees(request):
    data=mechanic.objects.all()
    return render(request,'admin/employees.html',{'data':data})
    
def admin_changepassword(request):
    return render(request,'admin/changepassword.html')
def admin_logout(request):
    return redirect('login')






   
   

   
   