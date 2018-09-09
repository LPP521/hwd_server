from django.conf.urls import url

from account import views

urlpatterns = [
    url(r'account/getUserInfo', views.getUserInfo),
    url(r'account/register', views.register),
    url(r'account/login', views.login),
    url(r'account/findPassword', views.findPassword),
]
