from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()

        return HttpResponse('Topics inserted successfully..')

    return render(request,'insert_topic.html')

def insert_webpage(request):
    lto=Topic.objects.all()
    d={'topics':lto}

    if request.method=='POST':
        tname=request.POST['tname']
        name=request.POST.get('name')
        url=request.POST['url']
        email=request.POST['email']
        to=Topic.objects.get(topic_name=tname)

        wo=WebPage.objects.get_or_create(topic_name=to,name=name,url=url,email=email)[0]
        wo.save()

        return HttpResponse('Webpage inserted succefully..')

    return render(request,'insert_webpage.html',d)

def insert_records(request):
    lwo=WebPage.objects.all()
    d={'webs':lwo}

    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        wo=WebPage.objects.get(name=name)

        ao=AccessRecords.objects.get_or_create(name=wo,author=author,date=date)[0]
        ao.save()

        return HttpResponse('Records inseerted successfully..')

    return render(request,'insert_records.html',d)

def retrievedata(request):
    lto=Topic.objects.all()
    d={'topics':lto}
    if request.method=='POST':
        td=request.POST.getlist('tname')
        print(td)
        webqueryset=WebPage.objects.none()

        for i in td:
            webqueryset=webqueryset|WebPage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrievedata.html',d)


def checkbox(request):
    lto=Topic.objects.all()
    d={'topics':lto}

    return render(request,'checkbox.html',d)

def radiobutton(request):
    lto=Topic.objects.all()
    d={'topics':lto}

    return render(request,'radiobutton.html',d)

def update_webpage(request):
    lto=Topics.objects.all()
    d={'topics':lto}

    return render()
    