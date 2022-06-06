from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="主页"),
]