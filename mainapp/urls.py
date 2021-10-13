from django.urls import path
from . import views
urlpatterns = [
    #path('', views.home, name="home"),
    path('homenotification/', views.home, name="homenotification"),
    path('testnotification/', views.test, name="testnotification"),
]