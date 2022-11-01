from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Article
def myfunctioncall(request):
  return HttpResponse("hello world")

def myfunctionabout(request):
  return HttpResponse("About response")

def add(request,a,b):
  return HttpResponse(a+b)

def intro(request,name,age):
  mydictionary = {
    "name" : name,
    "age" : age
  }
  return JsonResponse(mydictionary)

def mysecondpage(request):
  return render(request, 'second.html')

def mythirdpage(request):
    var = "hello world"
    greeting = "hey how are you"
    fruits = ["apple","mango","banana"]
    num1 , num2 = 10 , 7
    ans = num1 > num2
    #print(ans)
    mydictionary = {
        "var" : var,
        "msg" : greeting,
        "myfruits" : fruits,
        "num1" : num1,
        "num2" : num2,
        "ans" : ans
    }
    return render(request,'third.html',context=mydictionary)

def article_list(request):
  articles = Article.objects.all().order_by('date')
  return render(request, 'articles/article_list.html', {'articles': articles})
