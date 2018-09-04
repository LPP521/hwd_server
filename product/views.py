# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from account.base import baseResponse
from product.serializers import BannerSerializers
from product.models import Banner
# Create your views here.

@api_view(['GET'])
def getBannerList(request):
    banners = Banner.objects.all()
    serializer = BannerSerializers(banners, many=True)
    return baseResponse(200, serializer.data, 'success')