from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def hello(request):
    return render(request, "list.html")

def nice(request):
    return render(request, "lkh.html")