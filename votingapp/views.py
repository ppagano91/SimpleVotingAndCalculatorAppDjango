from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

arr=['Java','Python','C','C++','DotNET','JavaScript','PHP','Swift','SQL','R','D','Ruby','Delphi','Objective-C','Go','Java','Visual Basic','Perl','MATLAB',]
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

    # count=0
    # for element in globalcount:
    #     count=count+globalcount[element]["count"]

    # if query in globalcount:
    #     globalcount[query]["percentage"]=globalcount[query]["count"]/count
    # else:
    #     globalcount[query]["percentage"]=0

    mydict={
        "arr":arr,
        "globalcount":globalcount,

    }
    print(mydict)
    return render(request, "index.html",context=mydict)
    # return HttpResponse(query)
def sortdataascending(request):
    global globalcount
    globalcount = dict(sorted(globalcount.items(),key=lambda x: x[1]))

    mydict={
        "arr":arr,
        "globalcount":globalcount,
    }
    return render(request,"index.html",context=mydict)

def sortdatadescending(request):
    global globalcount
    globalcount = dict(sorted(globalcount.items(),key=lambda x: x[1], reverse=True ))

    mydict={
        "arr":arr,
        "globalcount":globalcount,
    }
    return render(request,"index.html",context=mydict)
