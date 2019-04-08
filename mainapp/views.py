from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import  get_template

# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html')


def about(request):
    #return render(request, 'mainapp/about.html')
    template = get_template(
        'mainapp/about.html'
    )
    return HttpResponse(
        template.render({
            'description':'О нашем магазине'
        })
    )



def contacts(request):
     contacts = ['Contact1','Contact2','Contact3']

     return render(
         request,
         'mainapp/contacts.html',
         {'contacts':contacts }
     )



def registr(request):
    return render(request, 'mainapp/registr.html')