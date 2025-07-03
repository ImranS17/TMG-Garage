from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Feedback, Complaint, BookService


# Create your views here.


def home(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        date = request.POST.get('date', '')
        message = request.POST.get('message', '')
        service = request.POST.get('service', '')
        feed = Feedback(name=name, date=date, message=message, service=service)
        feed.save()
        thank = True
        return render(request, 'home.html', {'thank':thank})
    return render(request, 'home.html')


def service(request):
    return render(request, 'service.html')


def about(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        date = request.POST.get('date', '')
        message = request.POST.get('message', '')
        service = request.POST.get('service', '')
        feed = Feedback(name=name, date=date, message=message, service=service)
        feed.save()
        thank = True
        return render(request, 'about.html', {'thank':thank})
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        contact = Complaint(name=name, email=email, phone=phone, message=message)
        contact.save()
        thank = True
        return render(request, 'contact.html', {'thank':thank})
    return render(request, 'contact.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid login')
            return redirect('Services:login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('Services:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('Services:register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User Created')
                return redirect('Services:login')
       
        else:
            messages.info(request,'Password not matching..')
            return redirect('Services:register')
        return redirect('/')
        

    else:    
        return render(request, 'register.html')

    
def logout(request):
    auth.logout(request)
    return redirect('/')



@login_required(login_url='Services:login')
def book(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')
        car = request.POST.get('car', '')
        phone = request.POST.get('phone', '')
        licenseno = request.POST.get('licenseno', '')
        pincode = request.POST.get('pincode', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        book = BookService(items_json=items_json, date=date, time=time, car=car, phone=phone, licenseno=licenseno, pincode=pincode, name=name, email=email,  address=address)
        book.save()
        thank = True
        return render(request, 'book.html', {'thank':thank})
    return render(request, 'book.html')


    
