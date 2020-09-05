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
    return render(request, 'view.html', {'user': user})

def trans(request):
    Fsend= request.POST.get('sender')
    Frec= request.POST.get('reciever')
    Fam= request.POST.get('amount')

    FFF=list(User.objects.all().values('name'))

    l=[]
    for ff in FFF:
        l.append(list(ff.values()))
    print(l)
    l1=reduce(lambda x,y: x+y, l)



    up=None
    up2=None
    trn2=None
    trn=None
    rec=None
    sen=None
    if Fam==None:
        Fam=0
    if (int(Fam)<0):
        return HttpResponse("Enter valid amount")
    else:
        if (Fsend and Frec in l1):
            if request.method == 'POST':
                sender = request.POST.get('sender','')
                reciever = request.POST.get('reciever','')
                amount = request.POST.get('amount','')
                transfer = Transfer(sender=sender,reciever=reciever,amount=amount)
                transfer.save()
            sen=User.objects.get(name=str(Fsend).lower()).current_credit
            rec=User.objects.get(name=str(Frec).lower()).current_credit
            trn=(sen-int(Fam))
            trn2=(rec+int(Fam))
            up=User.objects.filter(name=str(Fsend).lower()).update(current_credit=trn)
            up2=User.objects.filter(name=str(Frec).lower()).update(current_credit=trn2)
        elif(Fsend and Frec not in l1):
            return HttpResponse("Please enter valid names from user list only and also check the names you entered for case sensitivity")

    return render(request, 'transaction.html', {'up':up,'up2':up,'trn2':trn2,'trn':trn,'sen':sen,'rec':rec,'l1':l1,'l':l,'FFF':FFF,'Fsend':Fsend,'Frec':Frec,'Fam':Fam})

def trview(request):
    tran=Transfer.objects.all()
    return render(request, 'records.html', {'tran':tran})
