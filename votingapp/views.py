from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

arr=['Java','Python','Java','C','C++','DotNET','JavaScript','PHP','Swift','SQL','R','D','Ruby','Delphi','Objective-C','Go','Java','Visual Basic','Perl','MATLAB',]
globalcount=dict()

def index(request):
    mydict={
        "arr":arr
    }
    return render(request,"index.html",context=mydict)

def getquery(request):
    query=request.GET['languages']

    if query in globalcount:
        # if already exist then increment the value
        globalcount[query]=globalcount[query]+1
    else:
        # first occurrence
        globalcount[query]=1
    mydict={
        "arr":arr,
        "globalcount":globalcount,

    }
    return render(request, "index.html",context=mydict)
    # return HttpResponse(query)

