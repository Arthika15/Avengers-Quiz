"""
URL configuration for Avengers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('start',views.start,name="start"),
    path('result',views.result,name="result"),
    path('next1',views.next1,name="next1"),
    path('next2',views.next2,name="next2"),
    path('next3',views.next3,name="next3"),
    path('next4',views.next4,name="next4"),
    path('index',views.index,name="index")
]
