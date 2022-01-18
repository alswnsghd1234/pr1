from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Pruser
from .forms import LoginForm
# Create your views here.

def home(request):
    user_id = request.session.get('user')
    
    if user_id:
        pruser = Pruser.objects.get(pk=user_id)
        return HttpResponse(pruser.username)
    
    return HttpResponse('Home')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
        
    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html') # templates 폴더를 바라보게 되어있음.
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        
        res_data = {}
        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            pruser = Pruser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            pruser.save()
        return render(request, 'register.html', res_data) 