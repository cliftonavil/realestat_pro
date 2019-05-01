from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
def register(request):
  if request.method == 'POST':
    #register User
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    #Check if password match

    if password == password2:
      #Check user name
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That user name is already taken!!!')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being useds!!!')
          return redirect('register')
        else:
          #looks good
          user = User.objects.create_user(username=username, password=password,  email=email, first_name=first_name, last_name=last_name)
          #Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered can login')
          return redirect('login')
 
    else:
      messages.error(request, 'Password do not match!!!')
      return redirect('register')

  else:
    return render(request,'accounts/register.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')

   #login User
    return
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now log out')
    return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')