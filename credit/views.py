from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Transfer
import math
from functools import reduce
# Create your views here.
def index(request):
    return render(request, 'index.html')

def UserView(request):
    user = User.objects.all()
    a=User.objects.get(name='mayuresh')
    b=a.current_credit
    c=User.objects.get(name="varun")
    d=c.current_credit
    e=(d-b)
    print(b)
    print(e)
    print(user)
    return render(request, 'view.html', {'user': user,'a':a,'b':b,'c':c,'d':d,'e':e})

def trans(request):
    
    if request.method == 'POST':
        sender = request.POST.get('sender','')
        reciever = request.POST.get('reciever','')
        amount = request.POST.get('amount','')
        transfer = Transfer(sender=sender,reciever=reciever,amount=amount)
        transfer.save()
    Fsend= request.POST.get('sender')
    Frec= request.POST.get('reciever')
    Fam= request.POST.get('amount')
    FFF=list(User.objects.all().values('name'))
    # print(FFF[0])
    l=[]
    for ff in FFF:
        l.append(list(ff.values()))
    print(l) 
    l1=reduce(lambda x,y: x+y, l)
    print(l1)
    print(Frec,Fsend,Fam)
    up=None
    up2=None
    trn2=None
    trn=None
    rec=None
    sen=None
    if Fsend and Frec in l1:
        sen=User.objects.get(name=Fsend).current_credit
        rec=User.objects.get(name=Frec).current_credit
        trn=(sen-int(Fam))
        trn2=(rec+int(Fam))
        up=User.objects.filter(name=Fsend).update(current_credit=trn)
        up2=User.objects.filter(name=Frec).update(current_credit=trn2)
        print(up)
        print(up2)
        print(trn2)
        print(trn)
        print(sen)
        print(rec)
        
    
        
           
    
             
    # Dam= User.objects.get(name='varun').current_credit
    # Cam=(Dam-int(Fam))
    # print(Fsend,Frec,Fam,Dam)
    # print(type(Dam))  
    # ccc= User.objects.filter(name='varun').update(current_credit=Cam) 
        
    return render(request, 'transaction.html', {'up':up,'up2':up,'trn2':trn2,'trn':trn,'sen':sen,'rec':rec,'l1':l1,'l':l,'FFF':FFF,'Fsend':Fsend,'Frec':Frec,'Fam':Fam})    

def trview(request):
    tran=Transfer.objects.all()
    return render(request, 'records.html', {'tran':tran})