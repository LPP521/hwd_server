from rest_framework import serializers
from product.models import HomeCategory
from product.models import Banner
from product.models import Category

class HomeCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = HomeCategory
        fields = ('typeId', 'typeName')

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('typeId', 'imageUrl', 'path', 'description')

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('index', 'categoryId', 'categoryName')