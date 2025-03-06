from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    memlist = Member.objects.all().values()
    template = loader.get_template('allmembers.html')
    
    context = {'memlist' : memlist}
    return HttpResponse(template.render(context,request))


def details(request , id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    
    
    context = {'mem' : mymember}
    return HttpResponse(template.render(context , request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

