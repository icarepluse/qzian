from django.shortcuts import render, redirect
from django.contrib import messages
from .genqustion import genqustion
from .forms import MyForm
from django.utils.crypto import get_random_string
from .dbset import usrreg
from .models import qustion,answer,optionAnser,TestAnswer,cmuser,tests
import random

# Create your views here.


def logins(request):
      context=''
      if request.method=="POST":
            username=request.POST.get('Username')
            password=request.POST.get('Password')
            sellers=cmuser.objects.filter(umail=username, upass=password ).values()
            if sellers.count() == 1:
                
                    current_user = sellers.get()['id']
                    request.session['fduser']= current_user
                    request.session['fdusrnam']= sellers.get()['unames']
                    return redirect('dashbord')
            else:
                context ='Invalid email or password'
      return render(request,'login.html',{'context': context})
def userregister(request):
     if request.method == 'POST':
        if usrreg(request):
            return redirect('logins')
        else:
            messages.error(request, "Something error.")
        
     return render(request,'register.html') 
def userhome(request):
        unicids=get_random_string(length=15)
        testids=get_random_string(length=15)
        request.session['testid']=testids
        if request.method == 'POST':
            request.session['unicids']=unicids
            
           # print(genqustion(request))
            if  genqustion(request)==1:
                uids=request.session.get('unicids')
                cats=qustion.objects.filter(unicid=uids).all()
                if cats.exists():  # Check if the QuerySet is not empty
                    first_object = cats[0]  # Get the first object
                    first_value = first_object.id  # Replace 'some_field' with your model's field name
                else:
                    first_value = None
                return redirect('Qustionhome',first_value)

        return render(request,'index.html')

def Qustionhome(request,value):
        logchek(request)
        uids=request.session.get('unicids')
        qstin=qustion.objects.filter(unicid=uids,id=value).values()
        otion=optionAnser.objects.filter(unicid=uids,key=qstin.get()['key']).values()
        answers=answer.objects.filter(unicid=uids,key=qstin.get()['key']).values()
       
        nxtid=get_next_record(request,qstin.get()['id'])

        if request.method == 'POST':
            
                    value1 = request.POST.get('op1')
                    value2 = request.POST.get('answer')
                    value3=""
                    if value1 == value2:
                         value3="true"
                    else:
                         value3="false"
                 
                    TstANser=TestAnswer()
                    TstANser.testkey=request.session.get('testid')
                    TstANser.qustion=request.POST.get('qstin')
                    TstANser.uanswer=value1
                    TstANser.answers=value2
                    TstANser.crect=value3
                    suss= TstANser.save()
                    nextqstin=request.POST.get('nxt')
                    if nextqstin=='None':
                         
                         return redirect('Result')
                    else:
                         return redirect('Qustionhome',nextqstin)
        
        return render(request,'quastion.html',{'q': qstin.all(),'option':otion.all(),'answer':answers.all(),'nctid':nxtid})
    

def get_next_record(request,current_id):
    # Get the current record
    uids=request.session.get('unicids')
  
    current_record = qustion.objects.filter(unicid=uids,id=current_id,).first()
    if current_record:
        # Get the next record based on the ID
        next_record = qustion.objects.filter(id__gt=current_id).order_by('id').first()
        if next_record:
           return next_record.id
    return None

def Result(request):
        logchek(request)
        uids=request.session.get('unicids')
        testids=request.session.get('testid')
        user= request.session.get('fduser')
        filtered_count = TestAnswer.objects.filter(testkey=testids).count()
        crntan=0
        
        queryset= TestAnswer.objects.filter(testkey=testids).all()
        anems=''
        for item in queryset:
            item.is_equal = item.uanswer == item.answers
            if item.is_equal:
                crntan+=1
            
        optin=tests()
        optin.user=user
        optin.key=testids
        optin.unicid=uids
        optin.totalq=filtered_count
        optin.crct=crntan 
        random_integer = random.randint(1, 10000)
        optin.testids=random_integer
        optin.save()    
            
        return render(request,'result.html',{'total':filtered_count,'crect':crntan})

    
def Fullbiew(request):
        logchek(request)
        if 'tid' in request.GET:
                 testids=request.GET['tid']
               
        else:
                
        
                testids=request.session.get('testid')
                
        allanswer = TestAnswer.objects.filter(testkey=testids).values()
        queryset= TestAnswer.objects.filter(testkey=testids).all()
        
      
        return render(request,'fullview.html',{'answer':allanswer.all()})
def dashbord(request):
        logchek(request)
        userid= request.session.get('fduser')
        allanswer = tests.objects.filter(user=userid).values()
      
        return render(request,'dash.html',{'q':allanswer.all()})

      

def resultbl(request):
        logchek(request)
        userid= request.session.get('fduser')
        allanswer = tests.objects.filter(user=userid).values()
        return render(request,'resulttbl.html',{'q':allanswer.all()})

def logout(request):
         request.session.flush()
         request.session.delete()
         
         return redirect('logins')
         
def logchek(request):
          if 'fdusrnam' in request.session:
                user_name = request.session['fdusrnam']
        # Session variable 'user_name' is set, do something with user_name
          else:
        # Session variable 'user_name' is not set
                user_name = None
         
                return redirect('logins')
              