from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def nandhu(request):
    return HttpResponse('nandhu is a chubby girl')
def friend(request):
    return HttpResponse('<img src="data:image/jpeg;base64,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">')
def nandhini(request):
    return HttpRequest('<marquee>hello<marquee>')
