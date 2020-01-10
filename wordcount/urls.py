
from . import view
from django.urls import path

urlpatterns = [
    path('',view.myfun),
    path('counts/',view.counts,name='count'),
    path('about/',view.abouts,name ='about')   
]
