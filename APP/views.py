from email.contentmanager import raw_data_manager
from multiprocessing import context
from django.shortcuts import render
from .models import Student

def index(request):
    template="index.html"
    context={}
    if request.method=="POST":
        english_accetpance = 85
        math_accetpance = 90
        it_accetpance = 70
        italian_acceptance = 75
        bioligy_accetpance = 50
        diakok = list(Student.objects.filter(student_id=request.POST['studentid']))
        if(len(diakok) >= 1):
            template="results.html"
            context={
                'studentname' : diakok[0].student_name,
                'studentid' : diakok[0].student_id,
                'studentpoints' : diakok[0].student_points,
                'english' : diakok[0].student_points >= english_accetpance,
                'math' : diakok[0].student_points >= math_accetpance,
                'it' : diakok[0].student_points >= it_accetpance,
                'italian' : diakok[0].student_points >= italian_acceptance,
                'bioligy' : diakok[0].student_points >= bioligy_accetpance,
            }
        else:
            context={'incorrect' : len(diakok) != 1}
    return render(request, template, context)

def results(request):
    template="results.html"
    context={}
    return render(request, template, context)

def import_data(request):
    template="import.html"
    context={}
    possible_states = 0
    if request.method=="POST":
        import_data = list(request.POST['input_data'].split(';'))
        if(len(import_data) == 3):
            Student.objects.create(student_name = import_data[0],student_id = import_data[1],student_points = import_data[2])
            possible_states==1
            context={'possible_states' : possible_states}
        else:
            possible_states==2
            context={'possible_states' : possible_states}
        
        
    return render(request, template, context)