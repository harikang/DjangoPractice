from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime
def test1(request):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    return HttpResponse(f"{year} 년 {month} 월 {day}일에 요청받았어요!")

def test2(request, no):
    print("argument type: ",type(no))
    return HttpResponse(f"{no} 출력됐어요!")

def test3(request,y,m,d):
    return HttpResponse(f"{y} 년 {m} 월 {d}일")