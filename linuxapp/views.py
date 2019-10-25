from django.shortcuts import render
from django.utils import encoding #smart_unicode
from urllib.parse import parse_qsl

from .models import Service

# Create your views here.

def index(req):
    return render(req, 'linuxapp/index.html')

def about(req):
    return render(req, 'linuxapp/about.html')

def addbread(req):
    if req.method == 'POST':
        post = req.POST
        files = req.FILES
        s = Service()
        s.image = post['image']
        s.title = post['title']
        s.detail = post['detail']
        s.save()
        services = Service.objects.all()
        print(services)
        return render(req, 'linuxapp/addbread.html', { 'services': services })
    else:
        print('aaaaa')
        services = Service.objects.all()
        print(services)
        return render(req, 'linuxapp/addbread.html', { 'services': services })
