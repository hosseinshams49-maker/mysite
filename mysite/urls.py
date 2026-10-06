"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path
from mysite.views import http_test,json_test
urlpatterns = [
    path('admin/', admin.site.urls),
    path('http-test', http_test),
    path('json-test',json_test)
=======
from django.urls import path , include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls'))
>>>>>>> dfbe9468a5ab81a1d8e08ae52d4309e1fd05372a
]
