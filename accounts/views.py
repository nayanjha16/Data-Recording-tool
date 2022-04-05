from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from . import forms, models


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/user/dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,
                                 password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/user/dashboard')
        else:
            return HttpResponse('<center> Incorrect credentials </center>')
    return render(request, 'accounts/login.html', {})


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == 'POST':
        signup_form = forms.signup_form(request.POST)
        access_form = forms.user_form(request.POST)
        if signup_form.is_valid() and access_form.is_valid():
            user = signup_form.save(commit=False)
            access = access_form.save(commit=False)
            pswd = access_form.cleaned_data['password']
            access.set_password(pswd)
            access.save()
            user.user = access
            user.save()
            return HttpResponseRedirect('/')
        else:
            resp = str(signup_form.errors) + " " + str(access_form.errors)
            context = {'errors': resp}
    return render(request, 'accounts/signup.html', {})
