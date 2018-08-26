# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import QueryDict
from models import User
from serializers import UserSerializer
from account.base import baseResponse

# Create your views here.
@api_view(['GET'])
def getAllUser(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def register(request):
    dict = get_parameter_dic(request)
    phone = dict.get('phone')
    password = dict.get('password')
    nickName = dict.get('nickName')
    try:
        user = User.objects.get(phone=phone)
        return baseResponse(201, None, '用户已存在')
    except User.DoesNotExist:
        user = User()
        user.phone = phone
        user.password = password
        user.nick_name = nickName
        user.avator_url = 'http://i1.umei.cc/uploads/tu/201611/82/x0bdpfosimv.jpg'
        user.save()
        return baseResponse(200, '', '注册成功')
    return Response(UserSerializer(user).data, status=200)

@api_view(['POST'])
def login(request):
    dict = get_parameter_dic(request)
    phone = dict.get('phone', '')
    password = dict.get('password', '')
    try:
        user = User.objects.get(phone=phone)
        if password == user.password:
            return baseResponse(200, UserSerializer(user).data, '登录成功')
        else:
            return baseResponse(200, None, '密码错误')
    except User.DoesNotExist:
        return baseResponse(200, None, '用户不存在')
    return Response('')

#获取参数
def get_parameter_dic(request, *args, **kwargs):
    if isinstance(request, Request) == False:
        return {}
    query_params = request.query_params
    if isinstance(query_params, QueryDict):
        query_params = query_params.dict()
    result_data = request.data
    if isinstance(result_data, QueryDict):
        result_data = request.data.dict()
    if query_params != {}:
        return query_params
    else:
        return result_data