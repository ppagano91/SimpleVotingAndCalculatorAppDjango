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
        answer=eval(query)
        res={
        'query':query,
        'answer':answer,
        'error':False,
        'result':True,
        }
        return render(request, "index.html",context=res)
    except:
        res={
        'query':query,
        'error':True,
        'result':False,
        }
        return render(request, "index.html",context=res)

    return HttpResponse(query)
    return JsonResponse(json)