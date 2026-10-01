from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_viwe(request):
    return HttpResponse('<h1>home page</h1>')

def about_viwe(request):
    return HttpResponse('<h1>about page</h1>')

def contact_viwe(request):
    return HttpResponse('<h1>contact page</h1>')


