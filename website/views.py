from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def index_viwe(request):
    return HttpResponse('home page')

def about_viwe(request):
    return HttpResponse('about page')

def contact_viwe(request):
    return HttpResponse('contact page')


