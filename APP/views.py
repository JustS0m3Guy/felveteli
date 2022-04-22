from multiprocessing import context
from django.shortcuts import render

def index(request):
    template="index.html"
    context={}
    return(request, template, context)