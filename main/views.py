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
        else:
            messages.error(request,{messages.error})
        
        
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
            messages.success(request,'Welcome!')
            return redirect('home')
        
        
        else:
            messages.info(request,'Username OR Password is Incorrect!')
    context = {'messages':messages}
    return render(request,'main/login.html', context)
    
        
            


def logoutUser(request):
    logout(request)
    return redirect('login') 
 

#@login_required(login_url='login')
#def profile(request):
 #   guest = request.user.guest
  #  form = UpdateProfileForm(instance=guest)
   # if request.method == 'POST':
    #    form = UpdateProfileForm(request.POST, request.FILES, instance=guest)
      #  if form.is_valid():
       #     form.save()
            
    
    #context = {'form':form}
    
    #return render(request,'main/profile.html',context)



@login_required(login_url='login')
def home(request):
    guests = Guest.objects.all()
    tasks = Task.objects.all()
    
    context = {'tasks':tasks, 'guests':guests}
    return render(request, "main/home.html", context) 
 
 
 
 
@login_required(login_url='login')
def contact(request):
    return render(request, "main/contact.html")



@login_required(login_url='login')
def about(request):
    return render(request, "main/about.html")





@login_required(login_url='login')
def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'main/task_form.html',context)

@login_required(login_url='login')
def UpdateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'main/task_form.html',context)

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
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
                messages.success(request, 'Profile updated successfully!')
            except Exception as e:
                print(f"Error saving form: {e}")
                messages.error(request, f'Error updating profile: {e}')
        else:
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    
    context = {'form': form}
    return render(request, 'main/profile.html', context)