from django.shortcuts import get_object_or_404, render,redirect
from .models import Department,Course,Form
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .forms import DepartmentForm
# Create your views here.
def index(request):
   dep=Department.objects.all()
   return render(request,'index.html',{'dep':dep})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        user=User.objects.create_user(username=username,password=password)
        if password !=cpassword:
            messages.info(request,"password not matched")
        else:
            user.save()
            return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid username or password")
    return render(request,'login.html')  

def form_create(request):
    form=DepartmentForm() 
    if request.method=='POST':
        
        form=DepartmentForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('confirm')
    return render(request,'form.html',{'form':form})      
    
def form(request,pk):
    form=get_object_or_404(Form,pk=pk)
    form=DepartmentForm(instance=form)
    if request.method=='POST':
        form=DepartmentForm(request.POST,instance=form)
        if form.is_valid():
            form.save()
            return redirect('form_change',pk=pk)
    return render(request,'form.html',{'form':form})  
def load_course(request):
    department_id=request.GET.get('department_id')
    courses=Course.objects.filter(department_id=department_id).all()
    return render(request,'course_dropdown.html',{'courses':courses})
    
def confirm(request):
    return render(request,'confirm.html')
def home(request):
    return render(request,'home.html')
def logout(request):
    auth.logout(request)
    return redirect('/') 