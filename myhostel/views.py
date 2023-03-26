
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render,get_list_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group, User
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import Towns, Hostel, Students
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def home(request, towns_slug=None):
    towns_page= None
    hostel = None
    if towns_slug != None:
        towns_page = get_list_or_404(Towns, slug =towns_slug)
        hostel = Hostel.objects.filter(towns=towns_page, available = True)
    else:
        hostel = Hostel.objects.all().filter(available=True)
    return render(request,'home.html', {'towns': towns_page, 'hostel': hostel})

def hostels(request, hostel_id):
    try:
        hostel = Hostel.objects.get( id = hostel_id)
        
    except Exception as e:
        raise e
    count = hostel.stock - Students.objects.filter(hostel = hostel.id).count()
    user= request.user 
    student = Students.objects.get(user_id = user.id)
    return render(request, 'hostels.html', {'hostel': hostel, 'count': count, 'student': student})

@login_required(login_url='./login')
def myacount(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        surname = request.POST['surname']
        phonenumber = request.POST['phonenumber']
        location = request.POST['location']
        medicalnumber = request.POST['medicalnumber']
        university = request.POST['university']
        course = request.POST['course']
        email = request.POST['email']
        parentname = request.POST['parentname']
        parentlastname = request.POST['parentlastname']
        parentsurname = request.POST['parentsurname']
        parentnumber = request.POST['parentnumber']

        user = request.user
        student = Students.objects.get(user_id = user.id)
        if not student:
           student = Students.objects.create(user_id = user.id)

        user.first_name = firstname
        user.last_name= lastname
        student.surname= surname
        student.phonenumber= phonenumber
        student.location = location
        student.medicalnumber=medicalnumber
        student.university=university
        student.course=course
        user.email= email
        student.parentname=parentname
        student.parentlastname=parentlastname
        student.parentsurname=parentsurname
        student.parentnumber=parentnumber

        user.save()
        student.save()
        return HttpResponse(reverse('myacount'))

    user = request.user
    student= Students.objects.get(user_id = user.id)
    return render(request, 'myacount.html', {'user':user, 'student' : student})

def signUpView(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(signup_user)
    else:
        form = RegisterUserForm()
    return render(request, 'signup.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signoutView(request):
    logout(request)
    return redirect('login')

@login_required(login_url='./login')
def settlement(request, hostel_id):
    user = request.user
    student = Students.objects.get(user_id = user.id)
    if not student.hostel:
        student.hostel = Hostel.objects.get(id = hostel_id)
        student.save()
    return HttpResponseRedirect(reverse('myacount'))

@login_required(login_url='./login')
def settlement_cancil(request):
    user = request.user
    student = Students.objects.get(user_id = user.id)
    if student.hostel:
        student.hostel = None
        student.save()
    return HttpResponseRedirect(reverse('myacount'))
    

