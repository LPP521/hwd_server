# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class HomeCategory(models.Model):
    typeId = models.CharField(max_length=10)
    typeName = models.CharField(max_length=20)
    def __unicode__(self):
        return self.typeName

class Banner(models.Model):
    typeId = models.CharField(max_length=10, default='0')
    imageUrl = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.description

#菜单
class Menu(models.Model):
    typeId = models.CharField(max_length=10)
    categoryId = models.CharField(max_length=10)
    menuTitle = models.CharField(max_length=20)
    menuImage = models.CharField(max_length=200)
    def __unicode__(self):
        return self.menuTitle

#侧边栏分类
class Category(models.Model):
    index = models.IntegerField(default=0)
    categoryId = models.CharField(max_length=20)
    categoryName = models.CharField(max_length=20)
    def __unicode__(self):
        return self.categoryName

class Product(models.Model):
    imageUrl = models.CharField(max_length=200)
    productType = models.IntegerField(default=0)
    productTitle = models.CharField(max_length=200)
    productPrice = models.CharField(max_length=10)
    discountPrice = models.CharField(max_length=10)
    salesCount = models.CharField(max_length=10)
    couponCount = models.CharField(max_length=10)
    commission = models.CharField(max_length=10)