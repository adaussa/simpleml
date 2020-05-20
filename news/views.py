from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from news.models import News

# Create your views here.
def news(request):
    news = News.objects.all()
    template = loader.get_template('news/news.html')
    context = {
        'news' : news
    }
    return HttpResponse(template.render(context, request))

def newsDetail(request):
    return HttpResponse("Hello world")