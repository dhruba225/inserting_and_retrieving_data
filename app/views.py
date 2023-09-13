from django.shortcuts import render
from app.models import *

# Create your views here.
from django.http import HttpResponse

from django.db.models.functions import Length
from django.db.models import Q


def insert_topic(request):
    tn=input('Enter Topic Name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    tn=input('Enter Topic Name: ')
    to=Topic.objects.get(topic_name=tn)
    to.save()
    n=input('Enter Name: ')
    u=input('Enter Url: ')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def insert_access_record(request):
    n=input('Enter Name: ')
    wo=Webpage.objects.get(name=n)
    wo.save()
    d=input('Enter Date: ')
    a=input('Enter Author Name: ')
    e=input('Enter email: ')
    ao=Access_Record.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
    ao.save()
    QSAO=Access_Record.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_access_record.html',d)


def display_topic(request):

    QSTO=Topic.objects.all()

    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
#displaying all data
    QSWO=Webpage.objects.all()
#displaying data according to condition
    QSWO=Webpage.objects.filter(topic_name='Cricket')
#displaying data using exclude method
    QSWO=Webpage.objects.exclude(topic_name='Cricket')
#ordering data in ascending and descending order(all() is not compulsory)
    QSWO=Webpage.objects.all().order_by('name')
    QSWO=Webpage.objects.all().order_by('-name')
#ordering data according to length
    QSWO=Webpage.objects.all().order_by(Length('url'))
    QSWO=Webpage.objects.all().order_by(Length('url').desc())


#Field Look-ups
#     
#like operaters(not case-sensitive)
    QSWO=Webpage.objects.filter(url__startswith='www')
    QSWO=Webpage.objects.filter(url__endswith='in')
    QSWO=Webpage.objects.filter(name__contains='r')
#in operator
    QSWO=Webpage.objects.filter(name__in=('Rohit','Virat'))
#REGEx
    QSWO=Webpage.objects.filter(url__regex=r'in$')

#Q-Object-'|'
    QSWO=Webpage.objects.filter(Q(name='Rohit') & Q(topic_name='Cricket'))

#Q-Object-'&'
    QSWO=Webpage.objects.filter(Q(name='Rohit') | Q(name='Virat'))
    

    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def display_access_record(request):

    QSAO=Access_Record.objects.all()
#greater_than

    d={'QSAO':QSAO}
    return render(request,'display_access_record.html',d)
