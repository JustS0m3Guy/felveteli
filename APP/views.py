from email.contentmanager import raw_data_manager
from multiprocessing import context
from django.shortcuts import render
from .models import Student

def index(request):
    template="index.html"
    context={}
    if request.method=="POST":
        diakok = list(Student.objects.filter(student_id=request.POST['studentid']))
        print(len(diakok))
        if(len(diakok) == 1):
            template="results.html"
        else:
            context={'incorrect' : len(diakok) != 1}
    return render(request, template, context)

def results(request):
    template="results.html"
    context={}
    return render(request, template, context)
    #english_accetpance = models.BooleanField(default=False)
    #math_accetpance = models.BooleanField(default=False)
    #it_accetpance = models.BooleanField(default=False)
    #english_accetpance = models.BooleanField(default=False)
    #italian_acceptance = models.BooleanField(default=False)

def import_data(request):
    template="import.html"
    context={}
    possible_states = 0
    if request.method=="POST":
        import_data = list(request.POST['input_data'].split(';'))
        if(len(import_data) == 3):
            Student.objects.create(student_name = import_data[0],student_id = import_data[1],student_points = import_data[2])
            possible_states+=1
            context={'possible_states' : possible_states}
        else:
            context={'possible_states' : possible_states}
        
        
    return render(request, template, context)