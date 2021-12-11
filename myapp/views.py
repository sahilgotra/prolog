from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from.forms import signupform, User, userloginform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
      form = userloginform(request=request, data=request.POST)
      if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Logged in succesfully')
          return redirect('/profile/')
          
    form = userloginform()
    return render(request, 'myapp/user_login.html', {'form':form})
  else:
    return HttpResponseRedirect('/profile/')


def user_signup(request):
  if request.method == 'POST':
    form = signupform(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Account Created succesfully.')
      return redirect('/signup/')
  else:
    form = signupform()
  return render(request, 'myapp/user_signup.html', {'form':form})


def profile(request):
  if request.user.is_authenticated:
    return render(request, 'myapp/profile.html', {'name':request.user})
  else:
   return HttpResponseRedirect('/')


def userlogout(request):
 logout(request)
 return HttpResponseRedirect('/')
 





 

