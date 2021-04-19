"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
#프로젝트 만들었으니 url에 따라서 각자 함수를 실행하고 그에 함수에 알맞는 템플릿파일을 랜더링해서 사용자에게 보여줄건데 그 사용자 가 들어온 URL이랑 뷰 함수를 매칭해주는 역할 
#클라이언트가 깃헙 url로 들어오면 url을 urls.py에서 받아서 urls패턴중에서 매칭되는걸 찾음 찾은다음에 찾은 패스안에서 여기서 지정해준 url의 매칭되는 뷰 함수를 실행해주는 것. ->urls.py의 역할 
