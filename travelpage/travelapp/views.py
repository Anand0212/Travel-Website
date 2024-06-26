from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import EventFull, Enroll, Confirm, Enqiury # ParticipantDetails
from math import ceil
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
import razorpay


# Create your views here.
def index(request):
    events = EventFull.objects.all()
    n = len(events)
    nslides = (n//3) + ceil((n/3) - (n//3))
    context = {'no_of_slides' : nslides, 'event' : events, 'range' : range(1,nslides)}
    return render(request, 'index.html', context)

def events(request):
    events = EventFull.objects.all()
    context = {'eventsList': events}
    return render(request, 'events.html', context)

def ilogin(request):
    context = {}
    if request.method == 'POST':
        user = request.POST['uname']
        password = request.POST['pass1']
        if user == '' or password == '':
            context['errmsg'] = 'Fields cannot be empty'
            return render(request, 'login.html', context)
        else:
            u = authenticate(username = user, password = password)
            if u is not None:
                login(request, u)
                return redirect('/')
            else:
                context['errmsg'] = 'Username & Password Not valid'
                return render(request, 'login.html', context)
    return render(request, 'login.html')

def register(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        c_p = request.POST['confirm_password']
        if User.objects.filter(username = username).exists():
            context['errmsg'] = 'User Already Registered'
            return render(request, 'register.html', context)
        elif username == '' or password == '' or c_p == '':
            context['errmsg'] = 'Fields cannot be empty'
            return render(request, 'register.html', context)
        elif password != c_p:
            context['errmsg'] = 'Password Does not match with confirm password'
            return render(request, 'register.html', context)
        else:
            user = User.objects.create(username = username)
            user.set_password(password)
            user.save()
            context['success'] = 'User registerd successfully'
            return render(request, 'register.html', context)
            

    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')
    

def contact(request):
    context = {}
    if request.method == "POST":
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        if name == '' or number == '' or email == '':
            context['errmsg'] = 'Fields cannot be empty'
            return render(request, 'contact.html', context )
        else:
            c = Enqiury.objects.create(name = name, phone_number = number, emial = email)
            c.save()
            context['success'] = "Thanks! We'll reach out to you shortly"
        return render(request ,'contact.html', context)
    return render(request, 'contact.html')
    

def catfilter(request, n):
    events = EventFull.objects.filter(e_category = n)
    context = {'eventsList': events}
    return render(request, 'events.html', context)

def locfilter(request, sid):
    events = EventFull.objects.filter(e_state = sid)
    context = {'eventsList' : events}
    return render(request, 'events.html', context)

def sortby(request, oid):
    print(oid)
    if oid == '0':
        events = EventFull.objects.order_by('-e_date').all()
    elif oid == '1':
        events = EventFull.objects.order_by('e_date').all()
    context = {'eventsList' : events}
    return render(request, 'events.html', context)

def edetails(request, eid):
    events = EventFull.objects.filter(id = eid)
    context = {'details': events}
    return render(request, 'edetails.html', context)


def ulogout(request):
    logout(request)
    return redirect('/')

def confirm(request):
    context = {}
    sum = 0
    c = Confirm.objects.filter(userid = request.user.id)
    for x in c:
        sum += x.participants * x.eid.e_price
    context['total'] = sum
    context['carts'] = c
    return render(request, 'confirm.html', context)

def eenroll(request, eid):
    context = {}
    if request.user.is_authenticated:
        u = User.objects.filter(id = request.user.id)
        e = EventFull.objects.filter(id = eid)
        q1 = Q(eid = e[0])
        q2 = Q(userid = u[0])
        c = Confirm.objects.filter(q1 & q2)
        context['details'] = e
        n = len(c)
        print(n)
        if n == 1:
            context['msg'] = 'Already Enrolled, go to order summary for confirmation'
            return render(request, 'edetails.html', context)
        else:
            cobj = Confirm.objects.create(eid = e[0], userid = u[0])
            cobj.save()
            context['msg'] = ('Enrolled')
            return render(request, 'edetails.html', context)
    else:
        return redirect('/ilogin')
   

def updateqty(request, x, cid):
    c = Confirm.objects.filter(id = cid)
    q = c[0].participants
    if x == '1':
        q = q + 1
    elif x == '0' and q > 1:
        q = q - 1
    c.update(participants = q)
    return redirect('/confirm')
    
def remove(request, cid):
    c = Confirm.objects.filter(id = cid)
    c.delete()
    return redirect('/confirm')


def makepayments(request):
    client = razorpay.Client(auth=("rzp_test_o2A6cxwwKHRTY6", "H4LXfYkLDap3b82NF19WCD2O"))
    orders=Confirm.objects.filter(userid=request.user.id)
    context={}
    context["orders"]=orders
    sum=0

    for x in orders:
        sum=sum+x.eid.e_price * x.participants
        orderid=x.eid

    data = { "amount": sum*100, "currency": "INR", "receipt": "orderid" }
    payment = client.order.create(data=data)
    context["payment"]=payment
    return render(request,"pay.html",context)


def paymentsuccess(request):
    return HttpResponse(" PAYMENT SUCCESS ")