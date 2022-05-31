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

    return HttpResponse(query)
    return JsonResponse(json)