from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def index_view(request):
    if request.method=='GET':
        return render(request,'redister.html')
    else:
        sname= request.POST.get('sname','')
        cname=request.POST.get('clsname','')
        coursenames=request.POST.getlist('coursename',[])

        a=register(sname,cname,*coursenames)

        if a:
            return HttpResponse('注册成功')
        return HttpResponse('注册失败')
def showall_view(request):
    cls= clazz.objects.all()

    return render(request,'showall.html',{'cls':cls})


def getstu_view(request):
    cno=request.GET.get('cno','')
    no=int(cno)
    stus=clazz.objects.get(cno=no).student_set.all()

    return render(request,'getlist.html',{'stus':stus})