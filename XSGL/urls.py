"""XSGL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from app import views
from django.conf.urls import url

path('', include('app.urls')),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('login/', views.login),
    path('welcome/', views.welcome),
    path('add/', views.add),
    path('delete/', views.delete),
    path('update/', views.update),
    path('select/', views.select),
    path('info/', views.info),
    path('bottom/', views.bottom),
    path('selgrade/', views.selgrade),
    path('gradeall/', views.gradeall),
    path('gradeone/', views.gradeone),
    path('grademajor/', views.grademajor),
    path('gradecourse/', views.gradecourse),
    path('gradecoursemajor/', views.gradecoursemajor),
    path('grademid/', views.grademid),
    path('gradefail/', views.gradefail),
    path('failresult/', views.failresult),
    path('mid/', views.mid),
    path('updategrade/', views.updategrade),
    path('addgrade/', views.addgrade),
    path('printc/', views.printc),
    path('deletegrade/', views.deletegrade)
]
