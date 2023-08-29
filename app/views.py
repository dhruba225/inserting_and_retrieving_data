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

    QSWO=Webpage.objects.all()

    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def display_access_record(request):

    QSAO=Access_Record.objects.all()

    d={'QSAO':QSAO}
    return render(request,'display_access_record.html',d)