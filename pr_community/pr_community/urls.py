"""pr_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pruser.views import home

urlpatterns = [
    path('admin/', admin.site.urls),# 이 코딩의 의미는 admin에서 받은 url주소를 여기로 끌고 와서 url/땡땡/땡땡 이런식으로 만들 수 있게 해줌.
    path('pruser/', include('pruser.urls')),
    path('board/', include('board.urls')),
    path('', home),
]
