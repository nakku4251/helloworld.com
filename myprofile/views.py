from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def top(request):
    context = {
        "name": "たろう",
    }
    html = loader.render_to_spring("myprofile/top.html", context=context,request=request)
    return HttpResponse(html)

def resume(request):
    return HttpResponse("職務履歴ページです！！！")
