# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import Banner, Menu, HomeCategory, Category, Product

# Register your models here.
admin.site.register(HomeCategory)
admin.site.register(Banner)
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Product)
