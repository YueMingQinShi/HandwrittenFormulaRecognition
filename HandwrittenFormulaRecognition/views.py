from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def upload(request):
    return render(request, 'upload.html')

def handwrite(request):
    return render(request, 'handwrite.html')
