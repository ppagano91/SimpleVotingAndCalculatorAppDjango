from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def submitquery(request):
    query = request.GET['query']
    json={
        'query':query
    }

    try:
        result=eval(query)
        res={
        'query':query,
        'result':result,
        'error':False,
        }
        return render(request, "index.html",context=res)
    except:
        res={
        'query':query,
        'error':True,
        }
        return render(request, "index.html",context=res)

    return HttpResponse(query)
    return JsonResponse(json)