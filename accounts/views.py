from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import auth


def login(request):
    if request.user.is_authenticated:
        return HttpResponse('<center>ALREADY LOGGED IN </center>')
    if request.method == 'POST':
        username = "".format(request.POST['username'])
        password = "".format(request.POST['password'])
        user = auth.authenticate(username=username,
                                 password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponse('<center> Login successfull </center>')
        else:
            return HttpResponse('<center> Incorrect credentials </center>')
    return render(request, 'accounts/login.html', {})
