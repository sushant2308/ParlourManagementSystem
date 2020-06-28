from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,CreateAppointment,Addservice
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.decorators import login_required
from .models import Services,Appointment
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# Create your views here.

@unauthenticated_user
def register(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group =Group.objects.get('customer')
            user.groups.add(group)
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created Log in now'+ username)
            
    else:
        form= UserRegisterForm()
   
    context={'form':form}
    return render(request,'register.html',context)

def index(request):
    context ={
        'services' : Services.objects.all()
    }
    return render(request,'index.html',context)

@unauthenticated_user
def login(request):
    

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            messages.info(request,f'Username or password is incorrect')
    context={}
    return render(request,'login.html',context)

@login_required
def logoutuser(request):
    logout(request)
    return redirect('index')





@unauthenticated_user
def adminl(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        if user is not None:
            if user.groups.filter(name = 'admin').exists():
                auth_login(request,user,)
                return redirect('viewappoint')
            else:
                messages.info(request,f'You are not admin')
        else:
            messages.info(request,f'Username or password is incorrect')
    context={}
    return render(request,'adminl.html',context)
    

@login_required
def profile(request):
    return render()

@login_required
@allowed_users(['admin'])
def addser(request):
    if request.method == 'POST':
        form=Addservice(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=Addservice()
    context={'form':form}
    return render(request,'addser.html',context)


@login_required
def appointment(request):
    
    if request.method=='POST':
        form= CreateAppointment(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,f'You are appointment is noted')
            return redirect('index')
            
        else:
            messages.info(request,f'You are appointment has error')    
            
    else:
        form= CreateAppointment()
   
    context={'form':form}

    return render(request,'appointment.html',context)


@login_required
@allowed_users(['admin'])
def viewappo(request):
    total = Appointment.objects.count()
    new = Appointment.objects.filter(status='Pending').count()
    context={'total':total,'new':new,'datas':Appointment.objects.all()}
    return render(request,'viewappo.html',context)


def Accept(request,pk):
    value=get_object_or_404(Appointment,pk=pk)
    value.status='Accepted'
    value.save(update_fields=['status'])
    return redirect('viewappo')

def Decline(request,pk):
    value=get_object_or_404(Appointment,pk=pk)
    value.status='Declined'
    value.save(update_fields=['status'])
    return redirect('viewappo')
   