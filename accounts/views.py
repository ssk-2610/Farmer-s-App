from django.shortcuts import render, redirect
from .models import User, VendorUser
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth.models import auth
from django.template import RequestContext
# Create your views here.

def logout(request):
  del request.session['is_Logged']
  return render(request, 'index.html')

def userLogin(request): 
  if request.method=='POST':
    userlist = User.objects.all()
    for user in userlist:
      if (user.password==request.POST['passwd'] and user.name == request.POST['username']):
        request.session.clear()
        request.session['is_Logged'] = True
        response = redirect('http://localhost:8000/')
        response.set_cookie('userloggedin', True)
        response.set_cookie('username', user.name)
        response.set_cookie('password', user.password)
        return response
      else:
        messages.info(request,"Invalid User Credentials")
        response = render(request, 'login.html')
        response.set_cookie('isLogged', False)
        return response

  else:
    return render(request, 'login.html')

def userRegister(request):
  if request.method == 'POST':
    user = User()
    user.name = request.POST['username']
    user.email = request.POST['email']
    user.password = request.POST['passwd']
    user.phone = request.POST['phone']
    user.address = request.POST['address']
    user.save()
    return redirect('/login')
  else: 
    return render(request, 'signup.html')
  
# Vendor SECTION
# Vendor Login
def vendorLogin(request): 
  if request.method=='POST':
    vendorlist = VendorUser.objects.all()
    name = ''
    for vendor in vendorlist:
      if (vendor.password==request.POST['passwd'] and vendor.name == request.POST['username']):
        request.session['vendor_is_logged'] = True
        response = redirect('http://localhost:8000/vendor/')
        response.set_cookie('vendorloggedin', True)
        response.set_cookie('vendorname', vendor.name)
        response.set_cookie('vendorpassword', vendor.password)
        return response
      else:
        messages.info(request,"Invalid Vendor Credentials")
        return render(request, 'vendor/vendor-login.html')

  else:
    return render(request, 'vendor/vendor-login.html')

def vendorRegister(request):
  if request.method == 'POST':
    vendoruser = VendorUser()
    vendoruser.name = request.POST['username']
    vendoruser.email = request.POST['email']
    vendoruser.password = request.POST['passwd']
    vendoruser.phone = request.POST['phone']
    vendoruser.address = request.POST['address']
    vendoruser.save()
    return render(request, 'vendor/vendor-login.html')
  else: 
    return render(request, 'vendor/vendor-signup.html')

def vendorChangepass(request): 
  return render(request,'vendor/vendor-changepass.html')