'''
author: Tresor Omari
'''
from django.shortcuts import render

def mainpage(request):
    '''mainpage function'''
    return render(request, 'mainpage.html')

def hello(request):
    '''hello function'''
    person = request.GET['name']
    if not person:
        return render(request, 'hello.html', {'name': 'stranger'})
    else:
        return render(request, 'hello.html', {'name':person})
