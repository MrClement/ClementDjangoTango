from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import context
from django.template.context import RequestContext
from rango.models import Category, Page


def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by("-likes")[:5]
    context_dict = dict(categories=category_list)

    for c in category_list:
        c.url = c.name.replace(' ', '_')

    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    return render_to_response('rango/about.html', context)

def category(request, category_name_url):
    context = RequestContext(request)
    category_name = category_name_url.replace('_', ' ')

    context_dict = dict(category_name=category_name)

    try:
        category = Category.objects.get(name=category_name)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context_dict, context)


