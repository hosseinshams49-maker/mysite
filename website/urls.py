
from django.urls import path
from website.views import *


urlpatterns = [
    path('' , index_viwe),
    path('about' , about_viwe),
    path('contact' , contact_viwe)
]