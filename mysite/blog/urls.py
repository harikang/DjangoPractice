from django.urls import path
from . import views

urlpatterns = [
    path('test1/', views.test1),
    #test1 url에 오면, views.test1을 접속하게 됨. 
    #하위 url은 /를 안붙여도 됨. 
    path('test2/<int:no>/', views.test2), #출력시 인자를 받을 때는 <>를 받아야함. 
    path('test3/<year>/<month>/<day>/',views.test3)
]
