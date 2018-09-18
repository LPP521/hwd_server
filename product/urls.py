from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^product/getHomeCategory', views.getHomeCategory),
    url(r'^product/getBannerList', views.getBannerList),
    url(r'^product/getMenuByType', views.getMenuByType),
    url(r'^product/getCategoryList', views.getCategoryList),
    url(r'^product/getProductList', views.getProductList)
]
