from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def index(request):
    arr=['Java','Python','Java','C','C++','DotNET','JavaScript','PHP','Swift','SQL','R','D','Ruby','Delphi','Objective-C','Go','Java','Visual Basic','Perl','MATLAB',]

    mydict={
        "arr":arr
    }
    return render(request,"index.html",context=mydict)

def getquery(request):
    query=request.GET['languages']
    return HttpResponse(query)

