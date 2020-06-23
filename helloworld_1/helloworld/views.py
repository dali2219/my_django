from django.shortcuts import render
from datetime import datetime

def index(request):
  context = {
    'current_date':datetime.now(),
    'title':'Home'
  }
  return render(request,'index.html',context)

def about(request):
  context = {
    'current_date':datetime.now(),
    'title':'About'
  }
  return render(request,'about.html',context)

def news(request):
  context = {
    'current_date':datetime.now(),
    'title':'news'
  }
  return render(request,'news.html',context)