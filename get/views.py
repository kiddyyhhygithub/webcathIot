#_*_coding:utf-8_*_
from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from django.core.cache import cache
def index(request):
    if request.method == 'GET':
        cache.set('key',request.GET.get('value'),30)
    return HttpResponse(cache.get('key'))