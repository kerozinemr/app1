from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms import *
from .decorators import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


@unauthenticated_user
def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Welcome!')
            return redirect('login')
        
            
        
        
    context = {'form':form,'message':messages}
    return render(request,'main/register.html', context)


@unauthenticated_user
def loginPage(request):
      
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            
            return redirect('home')
        
        
        else:
            messages.info(request,'Username OR Password is Incorrect!')
    context = {'messages':messages}
    return render(request,'main/login.html', context)
    
        
            


def logoutUser(request):
    logout(request)
    return redirect('login') 
 


@login_required(login_url='login')
def home(request):
    guest = request.user.guest
    tasks = Task.objects.filter(guest=guest)
    context = {'tasks': tasks, 'guest': guest}
    return render(request, "main/home.html", context) 
 
 
 
 





@login_required(login_url='login')
def createTask(request):
    guest = request.user.guest
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False,)
            task.guest = guest
            task.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'main/task_form.html', context)

@login_required(login_url='login')
def UpdateTask(request):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'main/task_form.html',context)

@login_required(login_url='login')
def deleteTask(request):
    
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect('home')
    context = {'item':task}
    return render(request, 'main/delete.html',context)




@login_required(login_url='login')
def profile(request):
    guest = request.user.guest
    form = UpdateProfileForm(instance=guest)
    
    if request.method == 'POST':
        print("POST request received")
        print("FILES:", request.FILES)
        
        form = UpdateProfileForm(request.POST, request.FILES, instance=guest)
        if form.is_valid():
            print("Form is valid")
            try:
                form.save()
                print("Form saved successfully")
                
            except Exception as e:
                print(f"Error saving form: {e}")
                
        else:
            print("Form errors:", form.errors)
            
    
    context = {'form': form}
    return render(request, 'main/profile.html', context)