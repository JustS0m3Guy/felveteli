from multiprocessing import context
from django.shortcuts import render
from .models import Student

def index(request):
    template="index.html"
    context={}
    if request.method=="POST":
        diakok = list(Student.objects.filter(student_id=request.POST['studentid']))

        if(len(diakok) == 1):
            template="results.html"
        else:
            print("Helytelen azonosító!")
    return render(request, template, context)

def results(request):
    template="results.html"
    context={}
    return render(request, template, context)