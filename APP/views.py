from multiprocessing import context
from django.shortcuts import render

def index(request):
    template="index.html"
    context={}
    if request.method=="POST":
        if('studentid' == '11111111111'):
            template="results.html"
        else:
            print("Helytelen azonosító!")
    return render(request, template, context)

def results(request):
    template="results.html"
    context={}
    return render(request, template, context)