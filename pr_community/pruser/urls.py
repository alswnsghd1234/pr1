
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout)
]

import random

def number():
    ran_num = random.randint(1,45)
    return ran_num

randnum = []
while True:
    if len(randnum) == 6:
        break
    ran = number()
    if ran not in randnum:
        randnum.append(ran)
    
    
    
randnum.sort()
print(randnum, end='')