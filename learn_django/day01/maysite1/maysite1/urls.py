"""maysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,re_path
from .import views # .当前目录下


urlpatterns = [
    #http://127.0.0.1:8000
    path('admin/',admin.site.urls),
     #http://127.0.0.1:8000/page/1/
    path('page/<int:pag>/', views.pages_view),
    
    #http://127.0.0.1:8000/page/2003/
    # path('page/2003/',views.page_2003_view),
    # #path('<int:num1>/<str:func>/<int:num2>',views.func_view)
    # re_path(r'^(?P<num1>\d{1,2})/(?P<func>\[add|sub|mul])/(?P<num2>\d{1,2})',views.func_view),
    #http://127.0.0.1:8000/birthday/y/m/d
     re_path(r'^birthday/(?P<year>((19|20)\d{2}))/(?P<month>[1,2,3,4,5,6,7,8,9,10,11,12])/(?P<day>[1-9]|1\d|2\d|3[0,1]{1})',views.birthday_view)
     #不用正则表达式的时候 不需要(?P<>)
   
]
 