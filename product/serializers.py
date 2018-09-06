from rest_framework import serializers
from product.models import Banner
from product.models import Category

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'imageUrl', 'path', 'description')

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'index', 'categoryId', 'categoryName')