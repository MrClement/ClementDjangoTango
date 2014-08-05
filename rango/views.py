from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import context
from django.template.context import RequestContext


def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}

    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    return render_to_response('rango/about.html', context)