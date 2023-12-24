from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers=Member.objects.all().values()
    template =loader.get_template('all_members.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template .render(context,request))

def details(request,slug):
    mymember=Member.objects.get(slug=slug)
    template=loader.get_template('details.html')
    context={
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def main(requst):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())

def test(request):
    template=loader.get_template('test.html')
    context={
        'fruits':['Apple','Banna','Cherry'],
    }
    return HttpResponse(template.render(context,request))