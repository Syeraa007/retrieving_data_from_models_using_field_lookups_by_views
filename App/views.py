from django.shortcuts import render
# importing models
from App.models import *
# importing length function
from django.db.models.functions import Length
# importing Query object class
from django.db.models import Q

# Create your views here.
def display_topic(request):
    # using all method which show all data
    LTO=Topic.objects.all()
    # using filter method which show data of satisfied condition
    LTO=Topic.objects.filter(topic_name='Cricket')
    # LTO=Topic.objects.get(topic_name='Cricket')
    # Retrieving using field lookups
    LTO=Topic.objects.filter(topic_name__startswith='Volley')
    LTO=Topic.objects.filter(topic_name__endswith='Ball')
    LTO=Topic.objects.filter(topic_name__contains='bad')
    
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(name='Nani')
    # LWO=Webpage.objects.get(name='A')
    # Retrieving using field lookups
    # startswith,endswith,contains lookups are non-case-sensitive
    LWO=Webpage.objects.filter(name__startswith='sye')
    LWO=Webpage.objects.filter(url__endswith='in')
    LWO=Webpage.objects.filter(name__contains='h')
    LWO=Webpage.objects.filter(id__gt=8)
    LWO=Webpage.objects.filter(id__gte=10)
    LWO=Webpage.objects.filter(id__lt=3)
    LWO=Webpage.objects.filter(id__lte=5)

    d={'LWO':LWO}
    return render(request,'display_webpage.html',d)

def display_record(request):
    LAO=AccessRecord.objects.all()
    LAO=AccessRecord.objects.filter(author='Cutie')
    # LAO=AccessRecord.objects.get(author='A')
    # Retrieving using field lookups
    LAO=AccessRecord.objects.filter(author__startswith='N')
    LAO=AccessRecord.objects.filter(author__endswith='a')
    LAO=AccessRecord.objects.filter(author__contains='g')
    LAO=AccessRecord.objects.filter(date__gt='2020-11-11')
    LAO=AccessRecord.objects.filter(date__gte='2020-11-11')
    LAO=AccessRecord.objects.filter(date__lt='2021-09-24')
    LAO=AccessRecord.objects.filter(date__lte='2010-08-10')
    LAO=AccessRecord.objects.filter(date__year='2010')
    # we can use combination of 2 or more filed lookups in a single condition
    LAO=AccessRecord.objects.filter(date__year__gte='2010')
    LAO=AccessRecord.objects.filter(date__month__gte='08')
    LAO=AccessRecord.objects.filter(date__day__gte='20')
    # we can also use 2 condtions at a time using Query objects creation
    # for 'or' we use parallel-pipe('|') symbol and for 'and' we use ampersand('&')
    LAO=AccessRecord.objects.filter(Q(author='Nolan') | Q(date__year__gt='2015'))
    LAO=AccessRecord.objects.filter(Q(author='Nolan') & Q(date__year__lte='2001'))
    

    d={'LAO':LAO}
    return render(request,'display_record.html',d)