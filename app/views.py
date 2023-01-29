from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse

def insert_topic(request):
    tn=input('enter a topic name')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('topic is inserted successfully')

def insert_webpage(request):
    tn=input('enter a topic name ')
    name=input('enter a  name')
    url=input('enter url')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('webpage created successfully')

def insert_Accessrecords(request):
    tn=input('enter a topic name ')
    name=input('enter a  name')
    url=input('enter url')
    date=input('enter a date')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    A=Access_Records.objects.get_or_create(name=W,date=date)[0]
    A.save()
    return HttpResponse('accessrecords created successfully')

