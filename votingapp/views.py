from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

arr=['Java','Python','C','C++','DotNET','JavaScript','PHP','Swift','SQL','R','D','Ruby','Delphi','Objective-C','Go','Java','Visual Basic','Perl','MATLAB',]
globalcount=dict()
globalcount={'JavaScript': {'count': 5, 'percentage': '25.00'}, 'SQL': {'count': 2, 'percentage': '10.00'}, 'Python': {'count': 10, 'percentage': '50.00'},'Java': {'count': 3,
'percentage': '15.00'} }

def index(request):
    mydict={
        "arr":arr,
        "globalcount":globalcount,
    }
    return render(request,"index.html",context=mydict)

def getquery(request):
    print("request: ",request)
    query=request.GET['languages']

    if query in arr:
        if query in globalcount:        # if already exist then increment the value
            globalcount[query]["count"]=globalcount[query]["count"]+1

        else:
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
    else:
        # Se podría agregar mensaje de error: "Error en el ingreso de datos. Ingresar una opción válida"
        mydict={
            "arr":arr,
            "globalcount":globalcount,
        }
        return render(request, "index.html",context=mydict)
    # return JsonResponse(mydict)

def sortdataascending(request):
    global globalcount
    print("Descending Order")
    globalcount = dict(sorted(globalcount.items(),key=lambda x: x[1]["count"],reverse=False))

    mydict={
        "arr":arr,
        "globalcount":globalcount,
    }
    return render(request,"index.html",context=mydict)

def sortdatadescending(request):
    global globalcount
    print("Ascending Order")
    globalcount = dict(sorted(globalcount.items(),key=lambda x: x[1]["count"],reverse=True))


    mydict={
        "arr":arr,
        "globalcount":globalcount,
    }
    return render(request,"index.html",context=mydict)
