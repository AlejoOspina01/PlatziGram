""" Platzi Views """

#Debugger
import pdb;

# Django
from django.http.response import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    return HttpResponse('Hello anybody, Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))


def sort_integers(request):    
    """ pdb.set_trace() <-- sirve para probar sin recargar tanto la pagina"""
    numbers = sorted([int(number) for number in request.GET['numbers'].split(",")])
    response = JsonResponse(numbers, safe=False)
    return response

def say_hi(request,name,age):
    if age < 12:
        message = 'Sorry {},you are not allowed here'.format(name)
    else:
        message = 'Hello {}, Welcome to PlatziGram'.format(name)
    
    return HttpResponse(message)
