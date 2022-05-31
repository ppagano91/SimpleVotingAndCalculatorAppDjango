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

    if query in globalcount:        # if already exist then increment the value
        print("if")

        globalcount[query]["count"]=globalcount[query]["count"]+1
    else:
        print("else")
        # first occurrence
        globalcount[query]={}
        globalcount[query]["count"]=1

    count=0
    for element in globalcount:
        count=count+globalcount[element]["count"]

    for i in globalcount:
        globalcount[i]["percentage"]="{:.2f}".format((globalcount[i]["count"]/count)*100)


    mydict={
        "arr":arr,
        "globalcount":globalcount,
    }
    print(mydict)
    return render(request, "index.html",context=mydict)
    # return JsonResponse(mydict)
def sortdataascending(request):
    global globalcount
    print(globalcount.items())
    # globalcount = dict(sorted(globalcount[0].items(),key=lambda x: x[1]))

    mydict={
        "arr":arr,
        "globalcount":globalcount,
    }
    return render(request,"index.html",context=mydict)

def sortdatadescending(request):
    global globalcount
    # print(globalcount.items()[0][1].items())
    # globalcount = dict(sorted(globalcount[0].items(),key=lambda x: x[1], reverse=True ))

    mydict={
        "arr":arr,
        "globalcount":globalcount,
    }
    return render(request,"index.html",context=mydict)
