from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getquery', views.getquery, name='getquery'),
    path('sortdatadescending', views.sortdatadescending, name='sortdatadescending'),
    path('sortdataascending', views.sortdataascending, name='sortdataascending'),
]