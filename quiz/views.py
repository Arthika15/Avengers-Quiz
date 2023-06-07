from django.shortcuts import render
from .models import quizquestion,quizresult
from django.contrib import messages
# Create your views here.
# declaring score as a global variable
score=0
#calling the home page
def index(request):
    return render(request,"index.html")
# creating object based on id 
def start(request):
    name=request.POST['name']
    if len(name)==0:
        name="Avenger"
    quizquestions=quizquestion.objects.filter(id=1)
    #quizquestion1=quizquestion.objects()
    return render(request,'question1.html',{'name':name,'quizquestions':quizquestions})
def next1(request):
    global score
    score=0
    question1=request.POST['questions1']
    score=score+int(question1)
    quizquestions=quizquestion.objects.filter(id=2)
    return render(request,'question2.html',{'quizquestions':quizquestions,'score':score})
def next2(request):
    global score
    question2=request.POST['questions2']
    score=score+int(question2)
    quizquestions=quizquestion.objects.filter(id=3)
    return render(request,'question3.html',{'quizquestions':quizquestions,'score':score})
def next3(request):
    global score
    question3=request.POST['questions3']
    score=score+int(question3)
    quizquestions=quizquestion.objects.filter(id=4)
    return render(request,'question4.html',{'quizquestions':quizquestions,'score':score})
def next4(request):
    global score
    question4=request.POST['questions4']
    score=score+int(question4)
    quizquestions=quizquestion.objects.filter(id=5)
    return render(request,'question5.html',{'quizquestions':quizquestions,'score':score})
# based on score assigning the avengername
def result(request):
    global score
    question5=request.POST['questions5']
    score=score+int(question5)
    if score>= 5 and score<= 9:
        avengername="Iron Man" 
    elif score>= 10 and score<= 14:
        avengername="Black Widow"
    elif  score>= 15 and score<= 19:
        avengername="Captain America"
        
    elif score>= 20 and score<= 24:
        avengername="Thor"
    result=quizresult.objects.all()
    for res in result:
        if res.avengername==avengername:
            avengerdes=res.avengerdes
            avengerimg=res.avengerimg
            avenger={"avengername":avengername,"avengerdes":avengerdes,"avengerimg":avengerimg}
            return render(request,"submit.html",{'avenger':avenger,'score':score})   
        else:
            continue
   