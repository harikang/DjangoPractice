
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    #path(url, view) url로 들어오면 view로 특정작업을 함. 
    
    path("blog/",include("blog.urls")),
    #url로 들어오면, 앱/urls.py에 매핑한다. 
    #blog에 있는 urls로 접속
    path("applab/",include("applab.urls")),
    #url로 들어오면, applab/urls.py에 매핑한다. 
]
