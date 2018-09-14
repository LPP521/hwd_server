# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from account.base import baseResponse,get_parameter_dic
from product.serializers import HomeCategorySerializers, BannerSerializers, CategorySerializers,ProductSerializers
from product.models import HomeCategory, Banner, Category, Product
# Create your views here.

@api_view(['GET'])
def getBannerList(request):
    typeId = get_parameter_dic(request).get('typeId')
    if typeId == None:
        return baseResponse(201, None, 'typeId不能为空')
    banners = Banner.objects.filter(typeId=typeId)
    serializer = BannerSerializers(banners, many=True)
    return baseResponse(200, serializer.data, 'success')

@api_view(['GET'])
def getHomeCategory(request):
    homeCategorys = HomeCategory.objects.all()
    return baseResponse(200, HomeCategorySerializers(homeCategorys, many=True).data, 'success')

@api_view(['GET'])
def getCategoryList(request):
    categorys = Category.objects.all()
    categorySerialzier = CategorySerializers(categorys, many=True)
    return baseResponse(200, categorySerialzier.data, 'success')

@api_view(['GET'])
def getProductList(request):
    products = Product.objects.all()
    productSerialzier = ProductSerializers(products, many=True)
    return baseResponse(200, productSerialzier.data, 'success')
