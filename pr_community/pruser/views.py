from django.shortcuts import render
from .models import Pruser

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']
        
        pruser = Pruser(
            username=username,
            password=password
        )
        pruser.save()
        return render(request, 'register.html')